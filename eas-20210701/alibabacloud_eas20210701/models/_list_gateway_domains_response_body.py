# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class ListGatewayDomainsResponseBody(DaraModel):
    def __init__(
        self,
        custom_domains: List[main_models.ListGatewayDomainsResponseBodyCustomDomains] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The custom domain names.
        self.custom_domains = custom_domains
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.custom_domains:
            for v1 in self.custom_domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomDomains'] = []
        if self.custom_domains is not None:
            for k1 in self.custom_domains:
                result['CustomDomains'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_domains = []
        if m.get('CustomDomains') is not None:
            for k1 in m.get('CustomDomains'):
                temp_model = main_models.ListGatewayDomainsResponseBodyCustomDomains()
                self.custom_domains.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGatewayDomainsResponseBodyCustomDomains(DaraModel):
    def __init__(
        self,
        certificate_end_date: str = None,
        certificate_id: str = None,
        certificate_name: str = None,
        certificate_start_date: str = None,
        certificate_status: str = None,
        create_time: str = None,
        domain: str = None,
        type: str = None,
        update_time: str = None,
    ):
        self.certificate_end_date = certificate_end_date
        # The ID of the SSL certificate bound to the domain name. Obtain the certificate ID after you upload or purchase a certificate in the [Certificate Management Service](https://yundunnext.console.aliyun.com/?spm=5176.2020520163.console-base_help.2.4b3baJixaJixOc\\&p=cas) console.
        self.certificate_id = certificate_id
        self.certificate_name = certificate_name
        self.certificate_start_date = certificate_start_date
        self.certificate_status = certificate_status
        self.create_time = create_time
        # The custom domain name.
        self.domain = domain
        # The domain name type.
        # 
        # Valid value:
        # 
        # *   intranet: internal network.
        # *   internet: public network.
        self.type = type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_end_date is not None:
            result['CertificateEndDate'] = self.certificate_end_date

        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        if self.certificate_start_date is not None:
            result['CertificateStartDate'] = self.certificate_start_date

        if self.certificate_status is not None:
            result['CertificateStatus'] = self.certificate_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateEndDate') is not None:
            self.certificate_end_date = m.get('CertificateEndDate')

        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        if m.get('CertificateStartDate') is not None:
            self.certificate_start_date = m.get('CertificateStartDate')

        if m.get('CertificateStatus') is not None:
            self.certificate_status = m.get('CertificateStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

