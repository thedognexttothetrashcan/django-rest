# Day04





### ListView

- MultipleObjectTemplateResponseMixin
  - TemplateResponseMixin
- BaseListView
  - MultipleObjectMixin
    - ContextMixin
  - View
    - dispatch



### DetailView

- SingleObjectTemplateResponseMixin
- BaseDetailView
  - SingleObjectMixin
    - ContextMixin
  - View







### Django-REST-Framework

- QuickStart
  - 实现流程
    - 创建序列化器
      - 将Json转成模型
      - 将模型转成Json
    - 创建了ViewSet
      - View的集合
      - 快捷生成增删改查的多种操作
    - 创建路由器
      - 自定的路由系统
  - 使用
    - API带界面可浏览
    - 也可以直接操作使用
    - 注册的路由直接提供了增删改查，还提供了详情





### Serializer

- 功能
  - 对象转换成Dict
  - Dict转换对象
  - 数据序列化与反序列化

- HyperLinkedModelSerializer
  - 带超链接模型的序列化器
- Serializer
  - 必须实现抽象方法
    - update
      - 更新
    - create
      - 创建
  - 其余字段声明
    - Field
      - 初始化属性
        - read_only
        - write_only
        - required
        - default
        - initial
        - source
          - 映射
        - label
        - help_text
        - style
        - error_messages
        - validators
        - allow_null
    - BooleanField
      - 继承Field
        - 实现抽象方法
          - to_internal_value
          - to_representation
    - IntegerField
    - CharField
    - 和ORM声明非常像
  - ModelSerializer
    - 模型直接序列化
  - HyperLinkedModelSerializer
    - 模型序列化，添加超链接



### Views

- Request
  - 扩展了HttpRequest
  - request.data
    - 支持POST，PUT，PATCH
  - 使用组合搞定
- Response
  - TemplateResponse子类
  - 使用继承搞定
- status
  - 状态码
  - 编码更规范
- View转换
  - @api_view 装饰器包装原有的FBC，基于函数的视图函数
  - 继承APIView 实现，CBV，基于类的视图函数



### APIView

- as_view

- allowed_methods

- default_response_headers

- http_method_not_allowed

- permission_denied

- throttled

- get_authenticate_header

- get_parser_context

- get_render_context

- get_exception_handler_context

- get_view_name

- get_view_description

- get_format_suffix

- get_renders

- get_parsers

- get_authenticators

- get_permissions

- get_throttles

- get_content_negotitator

- get_exception_handler

- perform_content_negotiator

- perform_authentication

- check_permissions

- check_object_permissions

- check_throttles

- determine_version

- initalize_request

- initial

- finalize_response

- handle_exception

- raise_uncaught_exception

- dispatch

- options

  ## 执行流程

- as_view

  - super.as_view
  - 调用父类中as_view
    - dipatch(子类)
    - initalize_request(小核心)
      - request作为参数，又产出request
      - get_parser_context
      - get_parsers
      - get_authenticators
      - get_content_negotiator
      - 产出的request的是rest_framework中的request
        - 将Django中HttpRequest作为一个私有属性，存储在了自己的Request._request
    - default_response_headers
    - initial(大核心)
      - get_format_suffix 
      - perform_content_negotiation
      - determine_version
      - perform_authentication
      - check_permissions
      - check_throttles
    - 根据请求获取处理策略
      - 方法存在，调用方法的处理
      - 方法不存在，直接拒绝请求
        - http_method_not_allowed
      - 如果异常
        - handle_exception
    - finalize_response
    - csrf_exempt（view）
      - 所有REST接口豁免csrf
  - @api_view
    - 内部实际调用的还是APIView
    - 元编程构建APIView，设置各种属性，调用as_view



### APIView子类

#### generics

- GenericAPIView
  - 继承自View
  - get_queryset
  - get_object
  - get_serializer
  - get_serializer_class
  - get_serializer_context
  - filter_queryset
  - paginator_queryset
  - get_paginate_response
  - as_view
- CreateAPIView
  - GenericAPIView
  - mixins.CreateModelMixin
  - 实现了post
- ListAPIView
  - GenericAPIView
  - mixins.ListModelMixin
  - 实现了get
- RetrieveAPIView
  - GenericAPIView
  - mixins.RetrieveModelMixin
  - 实现get
- DestroyAPIView
  - GenericAPIView
  - mixins.DestroyModelMixin
  - 实现delete
- UpdateAPIView
  - GenericAPIView
  - mixins.UpdateModelMixin
  - 实现put
  - 实现patch
- ListCreateAPIView
  - GenericAPIView
  - mixins.ListModelMixin
  - mixins.CreateModelMixin
  - 实现了get
  - 实现了post
- RetrieveUpdateAPIView
  - GenericAPIView
  - mixins.RetrieveModelMixin
  - mixins.UpdateModelMixin
  - 实现了get
  - 实现了put
  - 实现了patch
- RetrieveDestroyAPIView
  - GenericAPIView
  - mixins.RetrieveModelMixin
  - mixins.DestroyModelMixin
  - 实现get
  - 实现delete
- RetrieveUpdateDestroyAPIView
  - GenericAPIView
  - mixins.RetrieveModelMixin
  - mixins.UpdateModelMixin
  - mixins.DestroyModelMixin
- 针对于复数
  - 创建
    - post
  - 获取
    - get
- 针对于单数
  - 获取
    - get
  - 更新
    - put
    - patch
  - 删除
    - delete



### mixins

- CreateModelMixin
  - create
    - get_serializer
    - perform_create
    - get_success_headers
  - perform_create
  - get_success_headers
- ListModelMixin
  - list
    - get_queryset
    - filter_queryset
    - paginate_queryset
    - get_serializer
    - 带分页
      - get_paginated_response
- RetrieveModelMixin
  - retrieve
    - get_object
    - get_serializer
- UpdateModelMixin
  - update
    - get_object
    - get_serializer
    - perform_update
  - perfom_update
  - partial_update
    - update
- DestroyModelMixin
  - destroy
    - get_object
  - perform_destroy



### homework

- 构建用户系统
- 构建博客系统
  - 只有登陆的用户才能创建博客
  - 博客创建自动绑定登陆用户





