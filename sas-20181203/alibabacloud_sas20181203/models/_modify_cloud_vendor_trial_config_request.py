# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCloudVendorTrialConfigRequest(DaraModel):
    def __init__(
        self,
        auth_id: int = None,
        auth_info: str = None,
        delete_trail: bool = None,
        vendor: str = None,
    ):
        # The ID of the audit log configuration to be modified.
        # > The ID can be queried via [DescribeCloudVendorAccountAKList](~~DescribeCloudVendorAccountAKList~~).
        # 
        # This parameter is required.
        self.auth_id = auth_id
        # Enter the multi-cloud configuration information:
        # - AWS: parameters sqsQueueName, sqsRegion
        # - Tencent: parameters kafkaUserName, kafkaBootstrapServers, kafkaTopic
        self.auth_info = auth_info
        # Whether to delete this audit log configuration:
        # - true: Delete
        # - false: Do not delete
        self.delete_trail = delete_trail
        # Cloud asset vendor. Values:
        # 
        # - **Tencent**: Tencent Cloud
        # - **AWS**: AWS
        # 
        # This parameter is required.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_id is not None:
            result['AuthId'] = self.auth_id

        if self.auth_info is not None:
            result['AuthInfo'] = self.auth_info

        if self.delete_trail is not None:
            result['DeleteTrail'] = self.delete_trail

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')

        if m.get('AuthInfo') is not None:
            self.auth_info = m.get('AuthInfo')

        if m.get('DeleteTrail') is not None:
            self.delete_trail = m.get('DeleteTrail')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

