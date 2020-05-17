# 自定义路由转换器

"""
复制原代码，把里面的正则表达式改一下
在总路由中，注册自定义路由转换器
"""
class MobileConverter:
  """自定义路由转换器：匹配手机号"""
  # 匹配手机号码的正则
  regex = '1[3-9]\d{9}'

  def to_python(self, value):
      # 将匹配结果传递到视图内部时使用
      return int(value)

  def to_url(self, value):
      # 将匹配结果用于反向解析传值时使用
      return str(value)