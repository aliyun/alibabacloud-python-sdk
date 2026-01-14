# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class AssociateAdditionalCertificatesWithListenerRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        certificates: List[main_models.AssociateAdditionalCertificatesWithListenerRequestCertificates] = None,
        client_token: str = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The GA instance ID.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The additional certificates.
        # 
        # You can specify up to 10 certificates in each request.
        # 
        # This parameter is required.
        self.certificates = certificates
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The listener ID. Only HTTPS listeners are supported.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The region ID of the GA instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.certificates:
            for v1 in self.certificates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.AssociateAdditionalCertificatesWithListenerRequestCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class AssociateAdditionalCertificatesWithListenerRequestCertificates(DaraModel):
    def __init__(
        self,
        domain: str = None,
        id: str = None,
    ):
        # The domain name that is specified by the certificate. You can associate each domain name with only one additional certificate.
        # 
        # You can specify up to 10 domain names in each request.
        # 
        # This parameter is required.
        self.domain = domain
        # The ID of the certificate. Only server certificates are supported.
        # 
        # You can specify up to 10 certificate IDs in each request.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

