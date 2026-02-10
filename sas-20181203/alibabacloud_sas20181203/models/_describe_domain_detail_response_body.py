# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainDetailResponseBody(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        domain: str = None,
        domain_detail_items: List[main_models.DescribeDomainDetailResponseBodyDomainDetailItems] = None,
        request_id: str = None,
        root_domain: str = None,
        vul_count: int = None,
    ):
        # The total number of alerts in your website assets.
        self.alarm_count = alarm_count
        # The domain name.
        self.domain = domain
        # An array that consists of the details about the domain asset.
        self.domain_detail_items = domain_detail_items
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The name of the root domain that corresponds to the domain.
        self.root_domain = root_domain
        # The total number of vulnerabilities in your website assets.
        self.vul_count = vul_count

    def validate(self):
        if self.domain_detail_items:
            for v1 in self.domain_detail_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count

        if self.domain is not None:
            result['Domain'] = self.domain

        result['DomainDetailItems'] = []
        if self.domain_detail_items is not None:
            for k1 in self.domain_detail_items:
                result['DomainDetailItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_domain is not None:
            result['RootDomain'] = self.root_domain

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        self.domain_detail_items = []
        if m.get('DomainDetailItems') is not None:
            for k1 in m.get('DomainDetailItems'):
                temp_model = main_models.DescribeDomainDetailResponseBodyDomainDetailItems()
                self.domain_detail_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootDomain') is not None:
            self.root_domain = m.get('RootDomain')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

class DescribeDomainDetailResponseBodyDomainDetailItems(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        uuid: str = None,
    ):
        # The type of the domain asset. Valid values:
        # 
        # *   **0**: an Elastic Compute Service (ECS) instance
        # *   **1**: a Server Load Balancer (SLB) instance
        # *   **2**: a Network Address Translation (NAT) gateway
        # *   **3**: an ApsaraDB RDS instance
        # *   **4**: an ApsaraDB for MongoDB instance
        self.asset_type = asset_type
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The name of the asset.
        self.instance_name = instance_name
        # The public IP address of the asset.
        self.internet_ip = internet_ip
        # The private IP address of the asset.
        self.intranet_ip = intranet_ip
        # The instance UUID of the domain asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

