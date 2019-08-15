# Day05



### 认证

- 什么是认证？
  - 用户身份登录验证
  - 根据提供的令牌找到用户
- REST-Framework
  - 根据令牌找到用户之后，把用户存在了Request上

- as_view
  - dispatch
    - initial
      - perform_authentication
        - request.user
          - 函数 -> 使用@Property
          - _authenticate()
            - authenticators 是Request构建来的
            - initialize_request 构建的Request
            - get_authenticators 获取构建时的认证器
            - authentication_classes 是APIView类属性
            - 认证成功会将登陆用户和令牌作为一个元组返回，否则返回None



### 权限

- 什么是权限
  - 代表操作某类，某种行为的一种限定
- REST-Framework
  - 通过用户身份判定是否具有某权限

- as_view
  - dispatch
    - initial
      - check_permissions
        - get_permissions
          - permission_classes
        - 对权限检查进行遍历
          - has_permission
          - 如果能通过权限检测，所有权限均满足
          - 有一个权限通不过，你就没有权限操作



### 权限认证总结

- 为什么实现
- 因为它们的是在dispatch中执行的
- 在get，post，delete等之前执行的
- 提前做了检测，验证
- 和中间件有啥区别？
  - 更具灵活性
  - 在指定的类中使用





### 级联

- 出错
  - 出去的序列化
  - 请求创建都是成功
  - 在响应的时候，对内容进行序列化







### 节流

- 频率控制
- 调用
  - as_view
    - initial
      - check_throttles
        - get_throttles获取所有节流器
        - 遍历判断
          - allow_request
        - 如果不允许
          - throttle.wait() 等多久
- throttling
  - BaseThrottle
    - allow_request
    - get_ident
    - wait
  - SimpleRateThrottle
    - 继承BaseThrottle
    - 函数
      - get_cache_key
      - get_rate
      - parse_rate
        - 根据 / 切割，最终转换成秒为单位
        - 次数/时间段
          - 时间段 s, m, h, d
      - allow_request
      - throttle_success
      - throttle_failure
      - wait
    - 执行流程
      - 入口
      - allow_request
        - get_cache_key
        - 根据key去缓存中获取请求序列
        - 数据清洗
          - 用当前时间减去时间区间
          - 时间节点值大于既有时间，既有时间被清除
        - 判断时间内的请求次数
          - 请求次数小于允许次数，允许请求
          - 请求次数大与允许次数，拒绝请求
  - AnonRateThrottle
    - 继承SimpleRateThrottle
  - UserRateThrottle
    - 继承SimpleRateThrottle
  - ScopedRateThrottle
    - 继承SimpleRateThrottle





### 节流

- 十秒之内只能搜索一次
  - 获取用户标识
    - ip
    - 用户令牌
  - 存入缓存
    - 值随便存，设置过期时间
  - 判断是否允许
    - 值存在，就不允许
    - 不存在，就允许
      - 将请求记录加入缓存
- 一分钟最多访问十次





### viewsets

- ViewSetMixin
  - as_view
  - initialize_request
  - reverse_action
  - get_extra_actions
  - get_extra_action_url_map
- ViewSet
  - 继承ViewSetMixin
  - 继承APIView
- GenericViewSet
  - 继承ViewSetMixin
  - 继承GenericAPIView
- ReadOnlyModelViewSet
  - 继承GenericViewSet
    - 继承ViewSetMixin
    - 继承GenericAPIView
  - RetrieveModelMixin
  - ListModelMixin

- ModelViewSet
  - 继承GenericViewSet
    - 继承ViewSetMixin
    - 继承GenericAPIView
  - 继承ListModelMixin
  - 继承RetrieveModelMixin
  - 继承UpdateModelMixin
  - 继承DestroyModelMixin
  - 继承CreateModelMixin





### homework

- 本周末
  - Django-REST-Framework总结成Xmin
  - 列出核心类
  - 列出核心方法
  - 数据走向（流程）
- 获取用户信息的时候，将用户的收货地址返回回来
  - 用户表
  - 地址表
  - 用户创建登陆
  - 地址创建，获取
  - 用户接口
    - 获取用户信息
    - 级联获取地址信息



