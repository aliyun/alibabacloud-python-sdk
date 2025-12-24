# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceMetadataOptionsRequest(DaraModel):
    def __init__(
        self,
        http_endpoint: str = None,
        http_put_response_hop_limit: int = None,
        http_tokens: str = None,
        instance_id: str = None,
        instance_metadata_tags: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # 
        # *   enabled
        # *   disabled
        # 
        # Default value: enabled.
        # 
        # >  For information about instance metadata, see [Obtain instance metadata](https://help.aliyun.com/document_detail/49122.html).
        # 
        # This parameter is required.
        self.http_endpoint = http_endpoint
        # >  This parameter is not publicly available.
        self.http_put_response_hop_limit = http_put_response_hop_limit
        # Specifies whether to forcefully use the security hardening mode (IMDSv2) to access instance metadata. Valid values:
        # 
        # *   optional: does not forcefully use the security hardening mode (IMDSv2).
        # *   required: forcefully uses the security hardening mode (IMDSv2). After you set this parameter to required, you cannot access instance metadata in normal mode.
        # 
        # Default value: optional.
        # 
        # >  For more information about modes of accessing instance metadata, see [Obtain instance metadata](https://help.aliyun.com/document_detail/150575.html).
        self.http_tokens = http_tokens
        # The ID of the instance.
        self.instance_id = instance_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # 
        # *   enabled
        # *   disabled
        # 
        # Default value: disabled.
        # 
        # >  The tag key must be a combination of letters, digits, @, colons (:), underscores (_), hyphens (-), periods (.), equal signs (=), and commas (,). The tag key cannot be "." or "..". Otherwise, the tag key cannot be accessed in the metadata.
        self.instance_metadata_tags = instance_metadata_tags
        self.owner_id = owner_id
        # The region ID of the instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint

        if self.http_put_response_hop_limit is not None:
            result['HttpPutResponseHopLimit'] = self.http_put_response_hop_limit

        if self.http_tokens is not None:
            result['HttpTokens'] = self.http_tokens

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_metadata_tags is not None:
            result['InstanceMetadataTags'] = self.instance_metadata_tags

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')

        if m.get('HttpPutResponseHopLimit') is not None:
            self.http_put_response_hop_limit = m.get('HttpPutResponseHopLimit')

        if m.get('HttpTokens') is not None:
            self.http_tokens = m.get('HttpTokens')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceMetadataTags') is not None:
            self.instance_metadata_tags = m.get('InstanceMetadataTags')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

