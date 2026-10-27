# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetIdentityProviderServiceProviderResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetIdentityProviderServiceProviderResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 失败时结合 HTTP 状态及 message 处理。
        self.code = code
        # 结果结构见本接口返回字段；异步写接口的返回表示受理，不保证后台任务已完成。
        self.data = data
        # 本次请求的处理状态，不等同后台任务最终结果。
        self.http_status_code = http_status_code
        # 请求受理或错误消息；异步任务结果需按对应查询接口核对。
        self.message = message
        # 用于关联本次调用与排障，失败时请保留。
        self.request_id = request_id
        # true 表示本次请求处理成功；异步写入仍需继续查询任务结果。
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetIdentityProviderServiceProviderResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetIdentityProviderServiceProviderResponseBodyData(DaraModel):
    def __init__(
        self,
        acs_url: str = None,
        entity_id: str = None,
        metadata_xml: str = None,
        protocol: str = None,
    ):
        # 我方 SAML 断言消费地址，配置到外部 IdP。
        self.acs_url = acs_url
        # 我方 SP 的实体标识，配置到外部 IdP；不是外部 IdP Entity ID。
        self.entity_id = entity_id
        # 我方 SP Metadata XML，供外部 IdP 导入；不能作为 IdP XML 提交 SAML 配置。
        self.metadata_xml = metadata_xml
        # 查询参数必填，仅支持精确值 SAML；响应返回 SAML。
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acs_url is not None:
            result['acsUrl'] = self.acs_url

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.metadata_xml is not None:
            result['metadataXml'] = self.metadata_xml

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acsUrl') is not None:
            self.acs_url = m.get('acsUrl')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('metadataXml') is not None:
            self.metadata_xml = m.get('metadataXml')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

