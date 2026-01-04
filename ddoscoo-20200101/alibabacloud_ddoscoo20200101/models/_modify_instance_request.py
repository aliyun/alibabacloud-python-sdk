# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        bandwidth: str = None,
        base_bandwidth: str = None,
        domain_count: str = None,
        edition_sale: str = None,
        function_version: str = None,
        instance_id: str = None,
        modify_type: str = None,
        normal_bandwidth: str = None,
        normal_qps: str = None,
        port_count: str = None,
        product_plan: str = None,
        product_type: str = None,
        service_bandwidth: str = None,
        service_partner: str = None,
    ):
        # Address type. Values:
        # - **Ipv4**: IPv4.
        # - **Ipv6**: IPv6.
        self.address_type = address_type
        # Elastic protection bandwidth (Mainland China). Unit: Gbps.
        self.bandwidth = bandwidth
        # Guaranteed protection bandwidth (Mainland China). Unit: Gbps.
        self.base_bandwidth = base_bandwidth
        # Number of protected domains.
        self.domain_count = domain_count
        # Protection package (Mainland China). Values:
        # 
        # - **coop**: Indicates the DDoS High Defense (Mainland China) Professional Edition.
        # - **advance**: Indicates the DDoS High Defense (Mainland China) Professional Edition.
        self.edition_sale = edition_sale
        # Function version, with values:
        # 
        # - **0**: Standard function.
        # - **1**: Enhanced function.
        self.function_version = function_version
        # The ID of the DDoS High Defense instance.
        # > You can call [DescribeInstanceIds](https://help.aliyun.com/document_detail/157459.html) to query the ID information of all DDoS High Defense instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Adjustment type, with values
        # - UPGRADE: Upgrade.
        # - DOWNGRADE: Downgrade.
        # 
        # This parameter is required.
        self.modify_type = modify_type
        # Business bandwidth (outside Mainland China). Unit: Mbps.
        self.normal_bandwidth = normal_bandwidth
        # Business QPS. Unit: Mbps.
        self.normal_qps = normal_qps
        # Number of protected ports.
        self.port_count = port_count
        # Protection package (outside Mainland China). Values:
        # 
        # - **0**: Indicates the DDoS High Defense (outside Mainland China) Insurance Edition.
        # - **1**: Indicates the DDoS High Defense (outside Mainland China) Worry-Free Edition.
        # - **2**: Indicates the DDoS High Defense (outside Mainland China) Acceleration Line.
        # - **3**: Indicates the DDoS High Defense (outside Mainland China) Secure Acceleration Line.
        self.product_plan = product_plan
        # Product type.
        # Values:
        # 
        # - **ddoscoo**: Indicates that the DDoS High Defense (Mainland China) instance is being adjusted for a China site account.
        # - **ddoscoo_intl**: Indicates that the DDoS High Defense (Mainland China) instance is being adjusted for an international site account.
        # - **ddosDip**: Indicates that the DDoS High Defense (outside Mainland China) instance is being adjusted for either a China or international site account.
        # 
        # This parameter is required.
        self.product_type = product_type
        # Business bandwidth (Mainland China). Unit: Mbps.
        self.service_bandwidth = service_bandwidth
        # Line resources of the instance (Mainland China). Values:
        # 
        # - **coop-line-001**: Indicates the DDoS High Defense (Mainland China) 8-line BGP line.
        self.service_partner = service_partner

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.base_bandwidth is not None:
            result['BaseBandwidth'] = self.base_bandwidth

        if self.domain_count is not None:
            result['DomainCount'] = self.domain_count

        if self.edition_sale is not None:
            result['EditionSale'] = self.edition_sale

        if self.function_version is not None:
            result['FunctionVersion'] = self.function_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.normal_bandwidth is not None:
            result['NormalBandwidth'] = self.normal_bandwidth

        if self.normal_qps is not None:
            result['NormalQps'] = self.normal_qps

        if self.port_count is not None:
            result['PortCount'] = self.port_count

        if self.product_plan is not None:
            result['ProductPlan'] = self.product_plan

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.service_bandwidth is not None:
            result['ServiceBandwidth'] = self.service_bandwidth

        if self.service_partner is not None:
            result['ServicePartner'] = self.service_partner

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('BaseBandwidth') is not None:
            self.base_bandwidth = m.get('BaseBandwidth')

        if m.get('DomainCount') is not None:
            self.domain_count = m.get('DomainCount')

        if m.get('EditionSale') is not None:
            self.edition_sale = m.get('EditionSale')

        if m.get('FunctionVersion') is not None:
            self.function_version = m.get('FunctionVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('NormalBandwidth') is not None:
            self.normal_bandwidth = m.get('NormalBandwidth')

        if m.get('NormalQps') is not None:
            self.normal_qps = m.get('NormalQps')

        if m.get('PortCount') is not None:
            self.port_count = m.get('PortCount')

        if m.get('ProductPlan') is not None:
            self.product_plan = m.get('ProductPlan')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ServiceBandwidth') is not None:
            self.service_bandwidth = m.get('ServiceBandwidth')

        if m.get('ServicePartner') is not None:
            self.service_partner = m.get('ServicePartner')

        return self

