一.基本简介
-------
1. 采用requests库，BasePage初始化时会读取config配置文件获取请求地址，
2. 对requests基础的get,post等请求做了封装，加入了日志
3. 把login也封装在底层，login会把登录信息（token）存放到属性中，在其他请求被调用时默认会带上登录信息,
4. api用来存放接口，抽象出参数,返回响应体
5. conftest.py 是全局的前置条件和后置条件，增加前后置不允许影响其他前后置方法运行，前置方法不允许报错
6. public_variable.py 为全局变量，conftest.py赋予的全局变量最好非必要不要修改，如需要变量请在其中定义
7. frame_constant.py 为全局常量，定义的常量无法被修改，仅适用于共有变量，谨慎添加
8. pip install -r requirements.txt 一键安装环境
9. 使用pytest标准，所有用例名称均为小写，类名为标准驼峰命名法，执行接口必要步骤需做步骤断言
10. 所有用例必须为test单词开头，否则框架无法识别用例
11. 过长的JSON数据不可放置在py文件中，请设置专门json文件格式存放于testdata目录下
12. 相同接口只允许存在一个既api目录下接口URL唯一，允许对已存在接口进行二次封装
13. Get、Post方法请求封装，携带token，sign信息
    注：使用此post/get替换json中的token，sign信息为前置登陆信息，
    若为独立项目请在config文件/单独方法 中独立配置账户信息

 二.使用
-------
1. 在API目录下先创建接口封装,再创建测试用例
例：
class  CaseApi:  # AllAPI类继承此类
    # API 接口封装
    @staticmethod
    auto_test_api_base(test_check_json):
        test_check = requests.post("/vms/login", test_check_json)
        return test_check
    # 可进行api接口二次封装,在用例层调用此封装
    auto_test_api_case(self, name, age, size)：
        test_check_json = { 
        参数1：name
        参数2：age
        参数3：size
      }
    # 相类下可用self，若在其他类下请引用封装类
    return self.auto_test_api_base(test_check_json)
    
    # Case层调用
class TestCase:
    "注明此类的用处"
    def test_case(self):
        test_check = all_api.auto_test_api_case('小明', 18, 180)
        # 断言此接口返回参数
        若为bool:
        assert test_check is True, f"预期：True, 实际：{test_check}"
        若为json:判断返回参数是否与入参相同
        assert test_check['name'] == '小明', 
            f"预期：test_check['name'] == '小明', 实际：{test_check['name']}"
        接口无返回参数：
            请在二次接口封装出注明无返回接口，如若是新增/删除/更新在调用完成后，
                请使用查询接口查询你新增/删除/更新后的数据是否正确

三.创建case和执行
-------
1. 在test目录下创建以test开头的py文件 例test_contract.py
2. 在test_contract.py 中创建类TestContract
例
'''
@pytest.fixture(scope='class',autouse=True)
def contract():         
    swap_create.create_Short("wangting_test_report")
    return "wangting_test_report"

3. 方法名也要以test开头(pytest规范)
4. 运行pytest -k "test" --html=TestReport.html --self-contained-html
