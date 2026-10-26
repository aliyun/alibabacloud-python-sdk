# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOperationTicketRequest(DaraModel):
    def __init__(
        self,
        approve_comment: str = None,
        asset_account_name: str = None,
        asset_id: str = None,
        effect_end_time: int = None,
        effect_start_time: int = None,
        instance_id: str = None,
        is_one_time_effect: bool = None,
        project_id: int = None,
        protocol_name: str = None,
        region_id: str = None,
    ):
        # The remarks of the request.
        # 
        # This parameter is required.
        self.approve_comment = approve_comment
        # The logon name of the asset account for which you want to request O&M access.
        # 
        # This parameter is required.
        self.asset_account_name = asset_account_name
        # The ID of the asset for which you want to request O&M access.
        # > You can call the [ListOperationDatabases](https://help.aliyun.com/document_detail/2758856.html) or [ListOperationHosts](https://help.aliyun.com/document_detail/2758857.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.asset_id = asset_id
        # The end time of the validity period for the logon request. Unit: seconds. The value is a UNIX timestamp.
        # > The end time of the validity period must be later than the start time.
        self.effect_end_time = effect_end_time
        # The start time of the validity period for the logon request. Unit: seconds. The value is a UNIX timestamp.
        self.effect_start_time = effect_start_time
        # The instance ID of the bastion host.
        # > You can invoke the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of logon times allowed. Valid values:
        # - **true**: Only one logon is allowed within the validity period.
        # - **false**: Unlimited logons are allowed within the validity period.
        self.is_one_time_effect = is_one_time_effect
        # The project ID.
        self.project_id = project_id
        # The name of the protocol for which you want to request O&M access. Valid values:
        # - SSH
        # - RDP
        # - MySQL
        # - PostgreSQL
        # - Oracle
        # - SQLServer
        # 
        # This parameter is required.
        self.protocol_name = protocol_name
        # The region ID of the bastion host.
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approve_comment is not None:
            result['ApproveComment'] = self.approve_comment

        if self.asset_account_name is not None:
            result['AssetAccountName'] = self.asset_account_name

        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.effect_end_time is not None:
            result['EffectEndTime'] = self.effect_end_time

        if self.effect_start_time is not None:
            result['EffectStartTime'] = self.effect_start_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_one_time_effect is not None:
            result['IsOneTimeEffect'] = self.is_one_time_effect

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApproveComment') is not None:
            self.approve_comment = m.get('ApproveComment')

        if m.get('AssetAccountName') is not None:
            self.asset_account_name = m.get('AssetAccountName')

        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('EffectEndTime') is not None:
            self.effect_end_time = m.get('EffectEndTime')

        if m.get('EffectStartTime') is not None:
            self.effect_start_time = m.get('EffectStartTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsOneTimeEffect') is not None:
            self.is_one_time_effect = m.get('IsOneTimeEffect')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

