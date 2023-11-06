import torch
from PIL import Image
from transformers import VisionEncoderDecoderModel
from transformers.models.nougat import NougatTokenizerFast
from src.app.nougat_models.nougat_latex import NougatLaTexProcessor

class NougatInference:
    def __init__(self):
        self.model_name = "Norm/nougat-latex-base"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # Initialize models, tokenizer, and latex processor
        self.model = VisionEncoderDecoderModel.from_pretrained(self.model_name).to(self.device)
        self.tokenizer = NougatTokenizerFast.from_pretrained(self.model_name)
        self.latex_processor = NougatLaTexProcessor.from_pretrained(self.model_name)
    def gat_nougat(self, image):


        image = Image.fromarray(image)
        image = image.convert("RGB")
        pixel_values = self.latex_processor(image, return_tensors="pt").pixel_values

        decoder_input_ids = self.tokenizer(self.tokenizer.bos_token, add_special_tokens=False,
                                          return_tensors="pt").input_ids
        with torch.no_grad():
            outputs = self.model.generate(
                pixel_values.to(self.device),
                decoder_input_ids=decoder_input_ids.to(self.device),
                max_length=self.model.decoder.config.max_length,
                early_stopping=True,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
                use_cache=True,
                num_beams=5,
                bad_words_ids=[[self.tokenizer.unk_token_id]],
                return_dict_in_generate=True,
            )
        sequence = self.tokenizer.batch_decode(outputs.sequences)[0]
        sequence = sequence.replace(self.tokenizer.eos_token, "").replace(self.tokenizer.pad_token, "").replace(
            self.tokenizer.bos_token, "")

        return sequence

