# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateEipInstanceRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        description: str = None,
        ens_region_id: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        internet_charge_type: str = None,
        ip_address: str = None,
        isp: str = None,
        name: str = None,
        tag: List[main_models.CreateEipInstanceRequestTag] = None,
    ):
        # The peak bandwidth of the EIP. Default value: 5. Valid values: 5 to 10000. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # Ensures the idempotence of the request to prevent duplicate operations caused by multiple retries.
        # 
        # - Generate a parameter value from your client and make sure that the value is unique among different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters in length.
        # 
        # - If you use a ClientToken that has been used before and the other request parameters remain unchanged, the client receives the same result as the first submission, without affecting the server-side state.
        # 
        # - You can retry when the API times out or returns the PROCESSING error code. Idempotence is effective in this case. If the response returns an HTTP 200 status code, the retry returns the same result as the previous call without affecting the server-side state. If the response returns an HTTP 4xx status code and the error code is not PROCESSING, idempotence is not effective.
        # 
        # - The ClientToken is valid for 10 minutes.
        self.client_token = client_token
        # The description.
        self.description = description
        # The ID of the Edge Node Service (ENS) edge zone.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # Billable methods of the EIP. Currently, only **PostPaid** (pay-as-you-go billing method) is supported.
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # The instance ID of the EIP.
        self.instance_id = instance_id
        # Billable methods of the EIP. Currently, only **95BandwidthByMonth** (monthly 95th percentile bandwidth billing) is supported.
        # 
        # This parameter is required.
        self.internet_charge_type = internet_charge_type
        # The IP address.
        self.ip_address = ip_address
        # The Internet service provider (ISP). Valid values:
        # 
        # - **cmcc**: China Mobile.
        # - **unicom**: China Unicom.
        # - **telecom**: China Telecom.
        self.isp = isp
        # The name of the EIP instance.
        self.name = name
        # The resource tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.name is not None:
            result['Name'] = self.name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateEipInstanceRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateEipInstanceRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance. Valid values of N: **1** to **20**.
        # 
        # - Cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # - Can be up to 64 characters in length.
        # - Cannot be an empty string.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`, or contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

