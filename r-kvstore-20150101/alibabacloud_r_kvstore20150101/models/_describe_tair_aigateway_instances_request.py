# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTairAIGatewayInstancesRequest(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        expired: str = None,
        instance_ids: str = None,
        instance_status: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        search_key: str = None,
        security_token: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The billing method. Valid values:
        # - **PostPaid**: pay-as-you-go
        self.charge_type = charge_type
        # The expiration status of the instance. Valid values:
        # 
        # * **true**: The instance has expired.
        # * **false**: The instance has not expired.
        self.expired = expired
        # The IDs of the instances to query.
        # > Separate multiple instance IDs with commas (,). You can specify up to 30 instance IDs in a single request.
        self.instance_ids = instance_ids
        # The instance status. Valid values:
        # * **Normal**: The instance is running.
        # * **Creating**: The instance is being created.
        # * **Changing**: The instance is being modified.
        # * **Inactive**: The instance is disabled.
        # * **Flushing**: The instance data is being purged.
        # * **Released**: The instance is released.
        # * **Transforming**: The instance is being transformed.
        # * **Migrating**: The instance is being migrated.
        # * **BackupRecovering**: The instance is recovering from a backup.
        # * **MinorVersionUpgrading**: The minor version of the instance is being upgraded.
        # * **NetworkModifying**: The network of the instance is being modified.
        # * **SSLModifying**: The SSL configuration of the instance is being modified.
        # * **MajorVersionUpgrading**: A major engine version upgrade is in progress. The instance remains accessible.
        # 
        # > For more information about instance statuses and impacts, see [Instance statuses and impacts](https://help.aliyun.com/document_detail/200740.html).
        self.instance_status = instance_status
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The search keyword. Fuzzy search is supported for instance names or instance IDs.
        self.search_key = search_key
        self.security_token = security_token
        # The ID of the vSwitch in the VPC. You can call the [DescribeVpcs](https://help.aliyun.com/document_detail/35739.html) operation to query the vSwitch ID.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.expired is not None:
            result['Expired'] = self.expired

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Expired') is not None:
            self.expired = m.get('Expired')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

