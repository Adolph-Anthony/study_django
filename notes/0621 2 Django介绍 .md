 ![django_logo](file:///E:/%E9%BB%91%E9%A9%AC/%E6%96%87%E4%BB%B6/django/01-Django%E6%A1%86%E6%9E%B6-%E7%AC%AC01%E5%A4%A9/1-%E6%95%99%E5%AD%A6%E8%B5%84%E6%96%99/Django%E8%AF%BE%E4%BB%B6%C2%A0/Django%E8%AF%BE%E4%BB%B6%C2%A0/images/django_logo.png) 



## 1.简介

1. Django，**发音为[`dʒæŋɡəʊ]**，是用python语言写的开源web开发框架，并遵循MVC设计。劳伦斯出版集团为了开发以新闻内容为主的网站，而开发出来了这个框架，于2005年7月在BSD许可证下发布。这个名称来源于比利时的爵士音乐家DjangoReinhardt，他是一个吉普赛人，主要以演奏吉它为主，还演奏过小提琴等。**由于Django在近年来的迅速发展，应用越来越广泛，被著名IT开发杂志SDTimes评选为2013SDTimes100，位列"API、库和框架"分类第6位，被认为是该领域的佼佼者。** 

   

2. Django的**主要目的是简便、快速的开发数据库驱动的网站。**它强调代码复用，多个组件可以很方便的以"插件"形式服务于整个框架，Django有许多功能强大的第三方插件，你甚至可以很方便的开发出自己的工具包。这使得Django具有很强的可扩展性。它还强调快速开发和DRY(DoNotRepeatYourself)原则。 



## 2.特点

### 2.1 重量级框架

对比Flask框架，Django原生提供了众多的功能组件，让开发更简便快速。

- 提供项目工程管理的自动化脚本工具

- 数据库ORM支持（对象关系映射，英语：Object Relational Mapping）
- 模板
- 表单
- Admin管理站点
- 文件管理
- 认证权限
- session机制
- 缓存





2.2 对比Flask框架，Django原生提供了众多的功能组件，让开发更简便快速。

- 提供项目工程管理的自动化脚本工具

- 数据库ORM支持（对象关系映射，英语：Object Relational Mapping）
- 模板
- 表单
- Admin管理站点
- 文件管理
- 认证权限
- session机制
- 缓存





### 2.2 MVT模式



有一种程序设计模式叫**MVC**，其核心思想是**分工、解耦，让不同的代码块之间降低耦合，增强代码的可扩展性和可移植性，实现向后兼容**。

> MVC的全拼为**Model-View-Controller**，最早由TrygveReenskaug在1978年提出，是施乐帕罗奥多研究中心(Xerox PARC)在20世纪80年代为程序语言Smalltalk发明的一种软件设计模式，是为了将传统的输入（input）、处理（processing）、输出（output）任务运用到图形化用户交互模型中而设计的。随着标准输入输出设备的出现，开发人员只需要将精力集中在业务逻辑的分析与实现上。后来被推荐为Oracle旗下Sun公司Java EE平台的设计模式，并且受到越来越多的使用ColdFusion和PHP的开发者的欢迎。现在虽然不再使用原来的分工方式，但是这种分工的思想被沿用下来，广泛应用于软件工程中，是一种典型并且应用广泛的软件架构模式。后来，MVC的思想被应用在了Ｗeb开发方面，被称为Ｗeb MVC框架。



#### MVC模式说明

![mvc](file:///E:/%E9%BB%91%E9%A9%AC/%E6%96%87%E4%BB%B6/django/01-Django%E6%A1%86%E6%9E%B6-%E7%AC%AC01%E5%A4%A9/1-%E6%95%99%E5%AD%A6%E8%B5%84%E6%96%99/Django%E8%AF%BE%E4%BB%B6%C2%A0/Django%E8%AF%BE%E4%BB%B6%C2%A0/images/mvc.png) 

- M全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行增、删、改、查操作。
- V全拼为View，用于封装结果，生成页面展示的html内容。
- C全拼为Controller，用于接收请求，处理业务逻辑，与Model和View交互，返回结果。

#### Django的MVT



![mvt](file:///E:/%E9%BB%91%E9%A9%AC/%E6%96%87%E4%BB%B6/django/01-Django%E6%A1%86%E6%9E%B6-%E7%AC%AC01%E5%A4%A9/1-%E6%95%99%E5%AD%A6%E8%B5%84%E6%96%99/Django%E8%AF%BE%E4%BB%B6%C2%A0/Django%E8%AF%BE%E4%BB%B6%C2%A0/images/mvt.png) 

- M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理。
- V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答。
- T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html。

**注：差异就在于黑线黑箭头标识出来的部分**