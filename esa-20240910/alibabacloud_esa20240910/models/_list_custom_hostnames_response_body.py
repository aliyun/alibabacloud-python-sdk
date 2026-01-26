# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListCustomHostnamesResponseBody(DaraModel):
    def __init__(
        self,
        hostnames: List[main_models.ListCustomHostnamesResponseBodyHostnames] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.hostnames = hostnames
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.hostnames:
            for v1 in self.hostnames:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hostnames'] = []
        if self.hostnames is not None:
            for k1 in self.hostnames:
                result['Hostnames'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hostnames = []
        if m.get('Hostnames') is not None:
            for k1 in m.get('Hostnames'):
                temp_model = main_models.ListCustomHostnamesResponseBodyHostnames()
                self.hostnames.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomHostnamesResponseBodyHostnames(DaraModel):
    def __init__(
        self,
        cert_apply_code: int = None,
        cert_apply_message: str = None,
        cert_http_key: str = None,
        cert_http_value: str = None,
        cert_not_after: str = None,
        cert_status: str = None,
        cert_txt_key: str = None,
        cert_txt_value: str = None,
        cert_type: str = None,
        conflict_with: str = None,
        create_time: str = None,
        hostname: str = None,
        hostname_id: int = None,
        offline_reason: str = None,
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
        # 免费证书申请错误码
        self.cert_apply_code = cert_apply_code
        # 免费证书申请错误说明
        self.cert_apply_message = cert_apply_message
        # 证书校验HTTP名称
        self.cert_http_key = cert_http_key
        # 证书校验HTTP内容
        self.cert_http_value = cert_http_value
        # 证书过期时间
        self.cert_not_after = cert_not_after
        self.cert_status = cert_status
        # 证书校验TXT名称
        self.cert_txt_key = cert_txt_key
        # 证书校验TXT内容
        self.cert_txt_value = cert_txt_value
        # 证书类型
        self.cert_type = cert_type
        self.conflict_with = conflict_with
        # 创建时间
        self.create_time = create_time
        # 用户自定义的主机名
        self.hostname = hostname
        self.hostname_id = hostname_id
        self.offline_reason = offline_reason
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
        if self.cert_apply_code is not None:
            result['CertApplyCode'] = self.cert_apply_code

        if self.cert_apply_message is not None:
            result['CertApplyMessage'] = self.cert_apply_message

        if self.cert_http_key is not None:
            result['CertHttpKey'] = self.cert_http_key

        if self.cert_http_value is not None:
            result['CertHttpValue'] = self.cert_http_value

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
        if m.get('CertApplyCode') is not None:
            self.cert_apply_code = m.get('CertApplyCode')

        if m.get('CertApplyMessage') is not None:
            self.cert_apply_message = m.get('CertApplyMessage')

        if m.get('CertHttpKey') is not None:
            self.cert_http_key = m.get('CertHttpKey')

        if m.get('CertHttpValue') is not None:
            self.cert_http_value = m.get('CertHttpValue')

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

