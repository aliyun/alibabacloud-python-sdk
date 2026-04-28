# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudWebcallRequest(DaraModel):
    def __init__(
        self,
        amd: int = None,
        clid: str = None,
        clid_area_code: str = None,
        clid_group: str = None,
        clid_list: str = None,
        crn_id: str = None,
        delay: int = None,
        enterprise_id: int = None,
        expir_time: str = None,
        ivr_id: int = None,
        multi_tel_delay: int = None,
        multi_tel_push: int = None,
        request_unique_id: str = None,
        retry: int = None,
        retry_interval: int = None,
        tel: str = None,
        timeout: int = None,
        user_field: str = None,
        vid: str = None,
    ):
        # 是否开启amd；自动应答检查（传真机等），1.开启 0.不开启 默认为0
        self.amd = amd
        # 可传入企业中继号码或设置好的客户侧外显号码
        self.clid = clid
        # 客户侧外显指定地区号码，优先级低于clid
        self.clid_area_code = clid_area_code
        # 客户侧外显号码组；使用clidGroup需要账号支持按标识路由，优先级低于clid
        self.clid_group = clid_group
        # 指定本次外呼使用的客户侧外显号码集合，系统将根据号码调度策略选择可用号码进行外呼
        self.clid_list = clid_list
        # 外显导航标识
        self.crn_id = crn_id
        # 延迟时长；秒数，延迟多少秒呼叫 参数取值范围：0<=delay<=60 默认为0
        self.delay = delay
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 过期时间，精确到s，yyyy-MM-dd HH:mm:ss
        self.expir_time = expir_time
        # 回呼接通后进入的ivrId；如果不传此参数，使用后台配置的ivr
        self.ivr_id = ivr_id
        # 多号码时呼叫延时；tel多个号码时，号码之间的呼叫延迟，最大120秒，默认0
        self.multi_tel_delay = multi_tel_delay
        # 多号码，是否每个号码呼叫都挂机推送；取值说明 0：只挂机推送一次； 1：每次呼叫都触发挂机推送；默认0
        self.multi_tel_push = multi_tel_push
        # 请求唯一标识；说明：长度不超过300个字节。1个汉字是3字节。此字段保存到通话记录requestUniqueId字段，后续接口查询使用。一次接口请求造成的多次呼叫requestUniqueId相同；如果是加密的号码，需要URLEncode后传入
        self.request_unique_id = request_unique_id
        # 重试次数；最大5次，使用的企业需要开启webcall自动重试开关
        self.retry = retry
        # 重试间隔，单位分钟，最小0分钟，最大59分钟
        self.retry_interval = retry_interval
        # 电话号码；固话带区号，手机不加0；固话带分机的以\\"-\\"分隔；支持多个号码，多个直接用英文逗号’,’分隔；传多个号码时，若前面的号码没接通则会呼叫后面的号码，若接通则不会呼叫；[加密外呼](../字段定义/接口部分/加密外呼号码加密规则.md)；如果是加密的号码，需要URLEncode后传入
        # 
        # This parameter is required.
        self.tel = tel
        # 呼叫客户超时时间；说明：参数取值范围 0<=timeout<=60；不传入，默认30(单位:s)
        self.timeout = timeout
        # 用户自定义字段；说明：长度不超过250个字节。1个汉字是3字节。此字段保存到通话记录userField字段，后续接口查询使用。该字段需“动态附带参数”paramNames有值时方可生效。
        self.user_field = user_field
        # 用哪种语言播放ivr提示音；1.普通话 2.粤语 4.标贝TTS 5.普通话-甜美女音 默认为1
        self.vid = vid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amd is not None:
            result['Amd'] = self.amd

        if self.clid is not None:
            result['Clid'] = self.clid

        if self.clid_area_code is not None:
            result['ClidAreaCode'] = self.clid_area_code

        if self.clid_group is not None:
            result['ClidGroup'] = self.clid_group

        if self.clid_list is not None:
            result['ClidList'] = self.clid_list

        if self.crn_id is not None:
            result['CrnId'] = self.crn_id

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.expir_time is not None:
            result['ExpirTime'] = self.expir_time

        if self.ivr_id is not None:
            result['IvrId'] = self.ivr_id

        if self.multi_tel_delay is not None:
            result['MultiTelDelay'] = self.multi_tel_delay

        if self.multi_tel_push is not None:
            result['MultiTelPush'] = self.multi_tel_push

        if self.request_unique_id is not None:
            result['RequestUniqueId'] = self.request_unique_id

        if self.retry is not None:
            result['Retry'] = self.retry

        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval

        if self.tel is not None:
            result['Tel'] = self.tel

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.user_field is not None:
            result['UserField'] = self.user_field

        if self.vid is not None:
            result['Vid'] = self.vid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amd') is not None:
            self.amd = m.get('Amd')

        if m.get('Clid') is not None:
            self.clid = m.get('Clid')

        if m.get('ClidAreaCode') is not None:
            self.clid_area_code = m.get('ClidAreaCode')

        if m.get('ClidGroup') is not None:
            self.clid_group = m.get('ClidGroup')

        if m.get('ClidList') is not None:
            self.clid_list = m.get('ClidList')

        if m.get('CrnId') is not None:
            self.crn_id = m.get('CrnId')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('ExpirTime') is not None:
            self.expir_time = m.get('ExpirTime')

        if m.get('IvrId') is not None:
            self.ivr_id = m.get('IvrId')

        if m.get('MultiTelDelay') is not None:
            self.multi_tel_delay = m.get('MultiTelDelay')

        if m.get('MultiTelPush') is not None:
            self.multi_tel_push = m.get('MultiTelPush')

        if m.get('RequestUniqueId') is not None:
            self.request_unique_id = m.get('RequestUniqueId')

        if m.get('Retry') is not None:
            self.retry = m.get('Retry')

        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')

        if m.get('Tel') is not None:
            self.tel = m.get('Tel')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UserField') is not None:
            self.user_field = m.get('UserField')

        if m.get('Vid') is not None:
            self.vid = m.get('Vid')

        return self

