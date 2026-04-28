# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudPreviewoutcallRequest(DaraModel):
    def __init__(
        self,
        backup_tels: str = None,
        call_variables: str = None,
        cdr_is_asr: int = None,
        clid_list: str = None,
        cno: str = None,
        crn_id: str = None,
        dial_tel_timeout: int = None,
        enterprise_id: int = None,
        is_investigation: int = None,
        ob_clid: str = None,
        ob_clid_area_code: str = None,
        ob_clid_group: str = None,
        request_unique_id: str = None,
        tel: str = None,
        timeout: int = None,
    ):
        # 备用外呼号码；tel没呼通时呼叫备用号码，最多支持5个号码，多个之间用逗号分隔
        self.backup_tels = backup_tels
        # 通道变量可以在以下场景中使用：1. 事件推送，作为推送字段使用2. 通话记录中，将字段存储在自定义字段3. 通过SIP-Header方式将字段传到呼叫的下游链路格式如: [{"name":"mainUniqueId","value":"cdr_main_unique_id","type":"2"},{"name":"callType","value":"cdr_call_type","type":"2"}]name：变量名称value：变量值type：变量类型，1.普通变量 2.PJSIP_HEADER变量（用于将变量通过SIP-Header方式传到客户侧，最多支持5个）
        self.call_variables = call_variables
        # 此次通话录音是否进行ASR转写；0.不进行 1.进行 默认：1
        self.cdr_is_asr = cdr_is_asr
        # 外显号码集合, 格式如: [{"clid":"1708587xxxx","priority":1},{"clid":"1304412xxxx","priority":2},{"clid":"0107990xxxx","priority":3}] clid：外显号码（String类型）（必填）priority：优先级（Integer类型）（非必填） 特别说明： 一次呼叫最多允许传10个指定号码；若指定了号码优先级，要求所有传入的号码都必传
        self.clid_list = clid_list
        # 座席工号；3-10位数字
        # 
        # This parameter is required.
        self.cno = cno
        # 外显导航标识
        self.crn_id = crn_id
        # 呼叫客户侧超时时间；取值范围 5<=dialTelTimeout<=60，默认45(单位:s)
        self.dial_tel_timeout = dial_tel_timeout
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 是否满意度调查；0.不进行满意度调查 1.进行满意度调查，默认：取企业配置
        self.is_investigation = is_investigation
        # 可传入企业中继号码或设置好的客户侧外显号码
        self.ob_clid = ob_clid
        # 指定外显区号；传入区号，在指定区号下外显号码；如果obClid和obClidAreaCode都传的情况下，按照obClid外显
        self.ob_clid_area_code = ob_clid_area_code
        # 客户侧外显号码组；使用clidGroup需要账号支持按标识路由，使用此参数时clid参数无效
        self.ob_clid_group = ob_clid_group
        # 请求唯一id；取值：如果没有传入值则系统会生产。如果是加密的号码，需要URLEncode后传入
        self.request_unique_id = request_unique_id
        # 需要进行呼叫的客户方电话号码，固话带区号，手机不加0。 当开启号码隐藏设置时，可从弹屏事件中获取customerNumberKey的值，进行外呼；[加密外呼](../字段定义/接口部分/加密外呼号码加密规则.md)；如果是加密的号码，需要URLEncode后传入；当外呼相关配置-支持分机号外呼开启后，此字段可支持传手机号-分机号格式
        # 
        # This parameter is required.
        self.tel = tel
        # 呼叫座席侧超时时间；取值范围 5<=timeout<=60，默认30(单位:s)
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_tels is not None:
            result['BackupTels'] = self.backup_tels

        if self.call_variables is not None:
            result['CallVariables'] = self.call_variables

        if self.cdr_is_asr is not None:
            result['CdrIsAsr'] = self.cdr_is_asr

        if self.clid_list is not None:
            result['ClidList'] = self.clid_list

        if self.cno is not None:
            result['Cno'] = self.cno

        if self.crn_id is not None:
            result['CrnId'] = self.crn_id

        if self.dial_tel_timeout is not None:
            result['DialTelTimeout'] = self.dial_tel_timeout

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.is_investigation is not None:
            result['IsInvestigation'] = self.is_investigation

        if self.ob_clid is not None:
            result['ObClid'] = self.ob_clid

        if self.ob_clid_area_code is not None:
            result['ObClidAreaCode'] = self.ob_clid_area_code

        if self.ob_clid_group is not None:
            result['ObClidGroup'] = self.ob_clid_group

        if self.request_unique_id is not None:
            result['RequestUniqueId'] = self.request_unique_id

        if self.tel is not None:
            result['Tel'] = self.tel

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupTels') is not None:
            self.backup_tels = m.get('BackupTels')

        if m.get('CallVariables') is not None:
            self.call_variables = m.get('CallVariables')

        if m.get('CdrIsAsr') is not None:
            self.cdr_is_asr = m.get('CdrIsAsr')

        if m.get('ClidList') is not None:
            self.clid_list = m.get('ClidList')

        if m.get('Cno') is not None:
            self.cno = m.get('Cno')

        if m.get('CrnId') is not None:
            self.crn_id = m.get('CrnId')

        if m.get('DialTelTimeout') is not None:
            self.dial_tel_timeout = m.get('DialTelTimeout')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('IsInvestigation') is not None:
            self.is_investigation = m.get('IsInvestigation')

        if m.get('ObClid') is not None:
            self.ob_clid = m.get('ObClid')

        if m.get('ObClidAreaCode') is not None:
            self.ob_clid_area_code = m.get('ObClidAreaCode')

        if m.get('ObClidGroup') is not None:
            self.ob_clid_group = m.get('ObClidGroup')

        if m.get('RequestUniqueId') is not None:
            self.request_unique_id = m.get('RequestUniqueId')

        if m.get('Tel') is not None:
            self.tel = m.get('Tel')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

