# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetCustomHostnameResponseBody(DaraModel):
    def __init__(
        self,
        custom_hostname_model: main_models.GetCustomHostnameResponseBodyCustomHostnameModel = None,
        request_id: str = None,
    ):
        self.custom_hostname_model = custom_hostname_model
        # 本次请求的唯一标识
        self.request_id = request_id

    def validate(self):
        if self.custom_hostname_model:
            self.custom_hostname_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_hostname_model is not None:
            result['CustomHostnameModel'] = self.custom_hostname_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHostnameModel') is not None:
            temp_model = main_models.GetCustomHostnameResponseBodyCustomHostnameModel()
            self.custom_hostname_model = temp_model.from_map(m.get('CustomHostnameModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCustomHostnameResponseBodyCustomHostnameModel(DaraModel):
    def __init__(
        self,
        cas_id: int = None,
        cert_apply_code: int = None,
        cert_apply_message: str = None,
        cert_http_key: str = None,
        cert_http_value: str = None,
        cert_id: str = None,
        cert_not_after: str = None,
        cert_status: str = None,
        cert_txt_key: str = None,
        cert_txt_value: str = None,
        cert_type: str = None,
        certificate: str = None,
        conflict_with: str = None,
        create_time: str = None,
        hostname: str = None,
        hostname_id: int = None,
        offline_reason: str = None,
        private_key: str = None,
        record_id: int = None,
        record_name: str = None,
        site_id: int = None,
        site_name: str = None,
        ssl_flag: str = None,
        status: str = None,
        update_time: str = None,
        verify_code: str = None,
        verify_host: str = None,
    ):
        self.cas_id = cas_id
        # 免费证书申请错误码
        self.cert_apply_code = cert_apply_code
        # 免费证书申请错误说明
        self.cert_apply_message = cert_apply_message
        # 证书校验HTTP名称
        self.cert_http_key = cert_http_key
        # 证书校验HTTP内容
        self.cert_http_value = cert_http_value
        self.cert_id = cert_id
        # 证书过期时间
        self.cert_not_after = cert_not_after
        # 证书状态
        self.cert_status = cert_status
        # 证书校验TXT名称
        self.cert_txt_key = cert_txt_key
        # 证书校验TXT内容
        self.cert_txt_value = cert_txt_value
        # 证书类型
        self.cert_type = cert_type
        # 上传的证书公钥
        self.certificate = certificate
        self.conflict_with = conflict_with
        # 创建时间
        self.create_time = create_time
        # 用户自定义的主机名
        self.hostname = hostname
        self.hostname_id = hostname_id
        self.offline_reason = offline_reason
        self.private_key = private_key
        # 绑定的源站记录ID
        self.record_id = record_id
        # 绑定的源站记录名
        self.record_name = record_name
        # 与主机名关联的站点ID
        self.site_id = site_id
        # 关联站点名称
        self.site_name = site_name
        # SSL开关的状态
        self.ssl_flag = ssl_flag
        # 自定义主机名状态
        self.status = status
        # 更新时间
        self.update_time = update_time
        # 归属校验TXT内容
        self.verify_code = verify_code
        # 归属校验TXT名称
        self.verify_host = verify_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cas_id is not None:
            result['CasId'] = self.cas_id

        if self.cert_apply_code is not None:
            result['CertApplyCode'] = self.cert_apply_code

        if self.cert_apply_message is not None:
            result['CertApplyMessage'] = self.cert_apply_message

        if self.cert_http_key is not None:
            result['CertHttpKey'] = self.cert_http_key

        if self.cert_http_value is not None:
            result['CertHttpValue'] = self.cert_http_value

        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cert_not_after is not None:
            result['CertNotAfter'] = self.cert_not_after

        if self.cert_status is not None:
            result['CertStatus'] = self.cert_status

        if self.cert_txt_key is not None:
            result['CertTxtKey'] = self.cert_txt_key

        if self.cert_txt_value is not None:
            result['CertTxtValue'] = self.cert_txt_value

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.conflict_with is not None:
            result['ConflictWith'] = self.conflict_with

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.hostname_id is not None:
            result['HostnameId'] = self.hostname_id

        if self.offline_reason is not None:
            result['OfflineReason'] = self.offline_reason

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.record_name is not None:
            result['RecordName'] = self.record_name

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.ssl_flag is not None:
            result['SslFlag'] = self.ssl_flag

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code

        if self.verify_host is not None:
            result['VerifyHost'] = self.verify_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasId') is not None:
            self.cas_id = m.get('CasId')

        if m.get('CertApplyCode') is not None:
            self.cert_apply_code = m.get('CertApplyCode')

        if m.get('CertApplyMessage') is not None:
            self.cert_apply_message = m.get('CertApplyMessage')

        if m.get('CertHttpKey') is not None:
            self.cert_http_key = m.get('CertHttpKey')

        if m.get('CertHttpValue') is not None:
            self.cert_http_value = m.get('CertHttpValue')

        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CertNotAfter') is not None:
            self.cert_not_after = m.get('CertNotAfter')

        if m.get('CertStatus') is not None:
            self.cert_status = m.get('CertStatus')

        if m.get('CertTxtKey') is not None:
            self.cert_txt_key = m.get('CertTxtKey')

        if m.get('CertTxtValue') is not None:
            self.cert_txt_value = m.get('CertTxtValue')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('ConflictWith') is not None:
            self.conflict_with = m.get('ConflictWith')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('HostnameId') is not None:
            self.hostname_id = m.get('HostnameId')

        if m.get('OfflineReason') is not None:
            self.offline_reason = m.get('OfflineReason')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RecordName') is not None:
            self.record_name = m.get('RecordName')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('SslFlag') is not None:
            self.ssl_flag = m.get('SslFlag')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')

        if m.get('VerifyHost') is not None:
            self.verify_host = m.get('VerifyHost')

        return self

