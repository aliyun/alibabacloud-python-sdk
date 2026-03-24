# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        get_domain_detail_model: main_models.DescribeCdnDomainDetailResponseBodyGetDomainDetailModel = None,
        request_id: str = None,
    ):
        # The details about the accelerated domain name.
        self.get_domain_detail_model = get_domain_detail_model
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.get_domain_detail_model:
            self.get_domain_detail_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_domain_detail_model is not None:
            result['GetDomainDetailModel'] = self.get_domain_detail_model.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetDomainDetailModel') is not None:
            temp_model = main_models.DescribeCdnDomainDetailResponseBodyGetDomainDetailModel()
            self.get_domain_detail_model = temp_model.from_map(m.get('GetDomainDetailModel'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdnDomainDetailResponseBodyGetDomainDetailModel(DaraModel):
    def __init__(
        self,
        cdn_type: str = None,
        cname: str = None,
        description: str = None,
        domain_name: str = None,
        domain_status: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        https_cname: str = None,
        resource_group_id: str = None,
        scope: str = None,
        server_certificate_status: str = None,
        source_models: main_models.DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels = None,
    ):
        # The workload type of the accelerated domain name. Valid values:
        # 
        # *   **web**: images and small files
        # *   **download**: large files
        # *   **video**: on-demand video and audio streaming
        self.cdn_type = cdn_type
        # The CNAME that is assigned to the accelerated domain name. You must add the CNAME record in the system of your DNS service provider to map the accelerated domain name to the CNAME.
        self.cname = cname
        # The description of the domain name.
        self.description = description
        # The accelerated domain name.
        self.domain_name = domain_name
        # The status of the accelerated domain name. Valid values:
        # 
        # *   **online**
        # *   **offline**
        # *   **configuring**
        # *   **configure_failed**
        # *   **checking**
        # *   **check_failed**
        # *   **stopping**
        # *   **deleting**
        self.domain_status = domain_status
        # The time when the domain name was created.
        self.gmt_created = gmt_created
        # The time when the domain name was last modified.
        self.gmt_modified = gmt_modified
        # The CNAME for which HTTPS is enabled.
        self.https_cname = https_cname
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The acceleration region.
        self.scope = scope
        # Indicates whether the SSL certificate is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.server_certificate_status = server_certificate_status
        self.source_models = source_models

    def validate(self):
        if self.source_models:
            self.source_models.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_type is not None:
            result['CdnType'] = self.cdn_type

        if self.cname is not None:
            result['Cname'] = self.cname

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_status is not None:
            result['DomainStatus'] = self.domain_status

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.https_cname is not None:
            result['HttpsCname'] = self.https_cname

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status

        if self.source_models is not None:
            result['SourceModels'] = self.source_models.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnType') is not None:
            self.cdn_type = m.get('CdnType')

        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainStatus') is not None:
            self.domain_status = m.get('DomainStatus')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HttpsCname') is not None:
            self.https_cname = m.get('HttpsCname')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')

        if m.get('SourceModels') is not None:
            temp_model = main_models.DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels()
            self.source_models = temp_model.from_map(m.get('SourceModels'))

        return self

class DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModels(DaraModel):
    def __init__(
        self,
        source_model: List[main_models.DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel] = None,
    ):
        self.source_model = source_model

    def validate(self):
        if self.source_model:
            for v1 in self.source_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SourceModel'] = []
        if self.source_model is not None:
            for k1 in self.source_model:
                result['SourceModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_model = []
        if m.get('SourceModel') is not None:
            for k1 in m.get('SourceModel'):
                temp_model = main_models.DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel()
                self.source_model.append(temp_model.from_map(k1))

        return self

class DescribeCdnDomainDetailResponseBodyGetDomainDetailModelSourceModelsSourceModel(DaraModel):
    def __init__(
        self,
        content: str = None,
        enabled: str = None,
        port: int = None,
        priority: str = None,
        type: str = None,
        weight: str = None,
    ):
        self.content = content
        self.enabled = enabled
        self.port = port
        self.priority = priority
        self.type = type
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.port is not None:
            result['Port'] = self.port

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

