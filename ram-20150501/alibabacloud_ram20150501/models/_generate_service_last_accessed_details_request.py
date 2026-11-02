# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateServiceLastAccessedDetailsRequest(DaraModel):
    def __init__(
        self,
        arn: str = None,
        granularity: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM identity for which you want to generate a permission audit report. Resource Access Management (RAM) users and regular RAM roles are supported.
        # 
        # Format:
        # - Resource Access Management (RAM) user: `acs:ram::<account_id>:user/<user_name>`
        # - RAM role: `acs:ram::<account_id>:role/<role_name>`
        # 
        # This parameter is required.
        self.arn = arn
        # The granularity of the permission audit report. Valid values:
        # - `SERVICE_LEVEL`: analyzes the permissions and access records of the RAM identity at the cloud service level. You can view the cloud service permissions granted to the RAM identity, the cloud services that the RAM identity has accessed, and the last access time for each cloud service. For more information about the cloud services that support service-level auditing, see [Cloud services that support permission auditing](https://www.alibabacloud.com/help/en/ram/cloud-services-that-support-permission-auditing).
        # - `ACTION_LEVEL`: analyzes the permissions and access records of the RAM identity at the API operation level, which provides a finer granularity than the service level. You can view the specific API operations that the RAM identity is authorized to perform and has performed. For more information about the cloud services that support operation-level auditing, see the cloud services whose **Audit granularity** is **Operation level** in [Cloud services that support permission auditing](https://www.alibabacloud.com/help/en/ram/cloud-services-that-support-permission-auditing).
        self.granularity = granularity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        return self

