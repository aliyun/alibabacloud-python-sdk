# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCloudVendorTrialConfigRequest(DaraModel):
    def __init__(
        self,
        auth_id: int = None,
        auth_info: str = None,
        vendor: str = None,
    ):
        # The unique ID of the AccessKey pair.
        # 
        # > You can call [DescribeCloudVendorAccountAKList](~~DescribeCloudVendorAccountAKList~~) to obtain the AuthId.
        # > -
        # 
        # This parameter is required.
        self.auth_id = auth_id
        # The multi-cloud configuration information:
        # - *AWS*: Input parameters sqsQueueName and sqsRegion.
        # - *Tencent*: Input parameters kafkaUserName, kafkaBootstrapServers, and kafkaTopic.
        # 
        # This parameter is required.
        self.auth_info = auth_info
        # The cloud asset vendor. Valid values:
        # 
        # - **Tencent**: Tencent Cloud.
        # - **HUAWEICLOUD**: Huawei Cloud.
        # - **Azure**: Azure.
        # - **AWS**: AWS.
        # - **VOLCENGINE**: Volcengine.
        # - **google**: Google Cloud.
        # - **CHAITIN**: Chaitin Technology.
        # - **FORTINET**: Fortinet.
        # - **THREATBOOK**: ThreatBook.
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

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthId') is not None:
            self.auth_id = m.get('AuthId')

        if m.get('AuthInfo') is not None:
            self.auth_info = m.get('AuthInfo')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

