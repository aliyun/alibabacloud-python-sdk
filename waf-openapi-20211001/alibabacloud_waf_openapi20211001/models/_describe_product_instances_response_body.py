# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeProductInstancesResponseBody(DaraModel):
    def __init__(
        self,
        product_instances: List[main_models.DescribeProductInstancesResponseBodyProductInstances] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the instances.
        self.product_instances = product_instances
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.product_instances:
            for v1 in self.product_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProductInstances'] = []
        if self.product_instances is not None:
            for k1 in self.product_instances:
                result['ProductInstances'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_instances = []
        if m.get('ProductInstances') is not None:
            for k1 in m.get('ProductInstances'):
                temp_model = main_models.DescribeProductInstancesResponseBodyProductInstances()
                self.product_instances.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeProductInstancesResponseBodyProductInstances(DaraModel):
    def __init__(
        self,
        access_instance_id: str = None,
        access_port_and_protocols: List[main_models.DescribeProductInstancesResponseBodyProductInstancesAccessPortAndProtocols] = None,
        access_ports: List[int] = None,
        owner_user_id: str = None,
        resource_instance_access_status: str = None,
        resource_instance_edition: str = None,
        resource_instance_id: str = None,
        resource_instance_ip: str = None,
        resource_instance_name: str = None,
        resource_ip: str = None,
        resource_name: str = None,
        resource_ports: List[main_models.DescribeProductInstancesResponseBodyProductInstancesResourcePorts] = None,
        resource_product: str = None,
        resource_region_id: str = None,
    ):
        self.access_instance_id = access_instance_id
        self.access_port_and_protocols = access_port_and_protocols
        self.access_ports = access_ports
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.owner_user_id = owner_user_id
        self.resource_instance_access_status = resource_instance_access_status
        self.resource_instance_edition = resource_instance_edition
        # The ID of the instance.
        self.resource_instance_id = resource_instance_id
        # The IP address of the instance that is added to WAF.
        self.resource_instance_ip = resource_instance_ip
        # The name of the instance that is added to WAF.
        self.resource_instance_name = resource_instance_name
        # The public IP address of the instance.
        self.resource_ip = resource_ip
        # The name of the instance.
        self.resource_name = resource_name
        # The information about the ports.
        self.resource_ports = resource_ports
        # The cloud service to which the instance belongs. Valid values:
        # 
        # *   **clb4**: Layer 4 CLB.
        # *   **clb7**: Layer 7 CLB.
        # *   **ecs**: ECS.
        self.resource_product = resource_product
        # The region ID of the instance. Valid values:
        # 
        # *   **cn-chengdu**: China (Chengdu).
        # *   **cn-beijing**: China (Beijing).
        # *   **cn-zhangjiakou**: China (Zhangjiakou).
        # *   **cn-hangzhou**: China (Hangzhou).
        # *   **cn-shanghai**: China (Shanghai).
        # *   **cn-shenzhen**: China (Shenzhen).
        # *   **cn-qingdao**: China (Qingdao).
        # *   **cn-hongkong**: China (Hong Kong).
        # *   **ap-southeast-3**: Malaysia (Kuala Lumpur).
        # *   **ap-southeast-5**: Indonesia (Jakarta).
        self.resource_region_id = resource_region_id

    def validate(self):
        if self.access_port_and_protocols:
            for v1 in self.access_port_and_protocols:
                 if v1:
                    v1.validate()
        if self.resource_ports:
            for v1 in self.resource_ports:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_instance_id is not None:
            result['AccessInstanceId'] = self.access_instance_id

        result['AccessPortAndProtocols'] = []
        if self.access_port_and_protocols is not None:
            for k1 in self.access_port_and_protocols:
                result['AccessPortAndProtocols'].append(k1.to_map() if k1 else None)

        if self.access_ports is not None:
            result['AccessPorts'] = self.access_ports

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.resource_instance_access_status is not None:
            result['ResourceInstanceAccessStatus'] = self.resource_instance_access_status

        if self.resource_instance_edition is not None:
            result['ResourceInstanceEdition'] = self.resource_instance_edition

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.resource_instance_ip is not None:
            result['ResourceInstanceIp'] = self.resource_instance_ip

        if self.resource_instance_name is not None:
            result['ResourceInstanceName'] = self.resource_instance_name

        if self.resource_ip is not None:
            result['ResourceIp'] = self.resource_ip

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        result['ResourcePorts'] = []
        if self.resource_ports is not None:
            for k1 in self.resource_ports:
                result['ResourcePorts'].append(k1.to_map() if k1 else None)

        if self.resource_product is not None:
            result['ResourceProduct'] = self.resource_product

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInstanceId') is not None:
            self.access_instance_id = m.get('AccessInstanceId')

        self.access_port_and_protocols = []
        if m.get('AccessPortAndProtocols') is not None:
            for k1 in m.get('AccessPortAndProtocols'):
                temp_model = main_models.DescribeProductInstancesResponseBodyProductInstancesAccessPortAndProtocols()
                self.access_port_and_protocols.append(temp_model.from_map(k1))

        if m.get('AccessPorts') is not None:
            self.access_ports = m.get('AccessPorts')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('ResourceInstanceAccessStatus') is not None:
            self.resource_instance_access_status = m.get('ResourceInstanceAccessStatus')

        if m.get('ResourceInstanceEdition') is not None:
            self.resource_instance_edition = m.get('ResourceInstanceEdition')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('ResourceInstanceIp') is not None:
            self.resource_instance_ip = m.get('ResourceInstanceIp')

        if m.get('ResourceInstanceName') is not None:
            self.resource_instance_name = m.get('ResourceInstanceName')

        if m.get('ResourceIp') is not None:
            self.resource_ip = m.get('ResourceIp')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        self.resource_ports = []
        if m.get('ResourcePorts') is not None:
            for k1 in m.get('ResourcePorts'):
                temp_model = main_models.DescribeProductInstancesResponseBodyProductInstancesResourcePorts()
                self.resource_ports.append(temp_model.from_map(k1))

        if m.get('ResourceProduct') is not None:
            self.resource_product = m.get('ResourceProduct')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        return self

class DescribeProductInstancesResponseBodyProductInstancesResourcePorts(DaraModel):
    def __init__(
        self,
        certificates: List[main_models.DescribeProductInstancesResponseBodyProductInstancesResourcePortsCertificates] = None,
        port: int = None,
        protocol: str = None,
    ):
        # The information about the certificates.
        self.certificates = certificates
        # The port number.
        self.port = port
        # The protocol type. Valid values:
        # 
        # *   **http**
        # *   **https**
        self.protocol = protocol

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
        result['Certificates'] = []
        if self.certificates is not None:
            for k1 in self.certificates:
                result['Certificates'].append(k1.to_map() if k1 else None)

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificates = []
        if m.get('Certificates') is not None:
            for k1 in m.get('Certificates'):
                temp_model = main_models.DescribeProductInstancesResponseBodyProductInstancesResourcePortsCertificates()
                self.certificates.append(temp_model.from_map(k1))

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeProductInstancesResponseBodyProductInstancesResourcePortsCertificates(DaraModel):
    def __init__(
        self,
        applied_type: str = None,
        certificate_id: str = None,
        certificate_name: str = None,
        domain: str = None,
    ):
        self.applied_type = applied_type
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The name of the certificate.
        self.certificate_name = certificate_name
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_type is not None:
            result['AppliedType'] = self.applied_type

        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppliedType') is not None:
            self.applied_type = m.get('AppliedType')

        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

class DescribeProductInstancesResponseBodyProductInstancesAccessPortAndProtocols(DaraModel):
    def __init__(
        self,
        certificate_ids: List[str] = None,
        port: int = None,
        protocol: str = None,
    ):
        self.certificate_ids = certificate_ids
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

