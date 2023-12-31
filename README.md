# 快速开始

1. 在python3.10环境下，项目的根目录执行如下命令安装依赖包。
   
   ```shell
   pip install -r requirements.txt
   ```


   


3. 确保test目录下的配置文件model_service.cfg中的配置项是正确的。
   
   *注意open ai的key
   
   *注意代理服务器配置
   
   *注意sam模型配置的路径   

4. 进入test目录运行如下命令启动三个独立微服务（在一台主机）。
   
   【windows环境】
   
   ```shell
   cd test
   set PYTHONPATH=..\src
   python test_scheduler.py
   ```
   
   ```shell
   cd test
   set PYTHONPATH=..\src
   python ..\src\app\routers\gpt.py
   ```
   
   ```shell
   cd test
   set PYTHONPATH=..\src
   python ..\src\app\routers\PaddleOCR.py
   ```
   
   【linux环境】
   
   ```shell
   cd test
   export PYTHONPATH=../src
   python test_scheduler.py
   ```
   
   ```shell
   cd test
   export PYTHONPATH=../src
   python ../src/app/routers/gpt.py
   ```
   
   ```shell
   cd test
   export PYTHONPATH=../src
   python ../src/app/routers/PaddleOCR.py
   ```

5. 访问[https://127.0.0.1:29081/docs](https://127.0.0.1:29081/docs) ，输入pic目录下图片测试。

# 已知问题

**1.在ubuntu环境部署，按本文件步骤报错from LLMChain不能import。**

**2. test_scheduler.py文件运行过程中报一个警告回调错误。**

**3. test_scheduler.py的工作进程容错不好，一旦出错无法承担新任务（比如openai进程无响应，则服务无法使用，即使openai恢复）。**



# 任务要求

# 任务要求

**1. 熟悉FastAPI的用法**

**2. 完成对图片的文字识别服务，并通过FastAPI以REST服务的方式对外提供**
具体要求：

- 通过POST方式上传图片到FastAPI
- FastAPI程序根据上传图片，调用PaddlePaddleOCR库识别文字
- 利用SAM对图像分割，同一分割区的文字归为同一类
- 把相邻文字整合到一段通过langchain，调用访问openai，提取要点（提词有参考）
- 因为识别、访问openai的时间比较长，为不影响服务，采用create_task，get_result的方法

**3. 测试pic目录下所有图片的识别结果**

**4. 对pic目录下所有图片运用SAM模型和OCR模型的识别结果分类注入openAI生成图片内容描述**

【参考与致谢】

- [Trickle的分析](https://github.com/PromptExpert/Trickle-On-WeChat/)
- [并发](https://fastapi.tiangolo.com/async/)
- [META](https://github.com/facebookresearch/segment-anything)
