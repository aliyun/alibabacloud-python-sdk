# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ApplyCoordinationForMonitoringRequest(DaraModel):
    def __init__(
        self,
        coordinate_policy_type: str = None,
        end_user_id: str = None,
        initiator_type: str = None,
        region_id: str = None,
        resource_candidates: List[main_models.ApplyCoordinationForMonitoringRequestResourceCandidates] = None,
        uuid: str = None,
    ):
        # The access policy during the remote assistance procedure.
        # 
        # This parameter is required.
        self.coordinate_policy_type = coordinate_policy_type
        # The ID of the end user who initiates the coordination flow. This parameter is not required if the request is initiated by an administrator.
        self.end_user_id = end_user_id
        # The initiator type.
        self.initiator_type = initiator_type
        # The region ID. You can call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of cloud computers that need to accept remote assistance.
        # 
        # This parameter is required.
        self.resource_candidates = resource_candidates
        # The UUID (unique identifier) of the device.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        if self.resource_candidates:
            for v1 in self.resource_candidates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coordinate_policy_type is not None:
            result['CoordinatePolicyType'] = self.coordinate_policy_type

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.initiator_type is not None:
            result['InitiatorType'] = self.initiator_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['ResourceCandidates'] = []
        if self.resource_candidates is not None:
            for k1 in self.resource_candidates:
                result['ResourceCandidates'].append(k1.to_map() if k1 else None)

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinatePolicyType') is not None:
            self.coordinate_policy_type = m.get('CoordinatePolicyType')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('InitiatorType') is not None:
            self.initiator_type = m.get('InitiatorType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.resource_candidates = []
        if m.get('ResourceCandidates') is not None:
            for k1 in m.get('ResourceCandidates'):
                temp_model = main_models.ApplyCoordinationForMonitoringRequestResourceCandidates()
                self.resource_candidates.append(temp_model.from_map(k1))

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class ApplyCoordinationForMonitoringRequestResourceCandidates(DaraModel):
    def __init__(
        self,
        owner_ali_uid: int = None,
        owner_end_user_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_properties: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The Alibaba Cloud account ID of the cloud computer administrator.
        # 
        # This parameter is required.
        self.owner_ali_uid = owner_ali_uid
        # The username of the current user of the cloud computer.
        # 
        # > This field is required.
        self.owner_end_user_id = owner_end_user_id
        # The cloud computer ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The cloud computer name.
        # 
        # This parameter is required.
        self.resource_name = resource_name
        # The properties of the cloud computer.
        self.resource_properties = resource_properties
        # The region where the resource resides.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_ali_uid is not None:
            result['OwnerAliUid'] = self.owner_ali_uid

        if self.owner_end_user_id is not None:
            result['OwnerEndUserId'] = self.owner_end_user_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_properties is not None:
            result['ResourceProperties'] = self.resource_properties

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerAliUid') is not None:
            self.owner_ali_uid = m.get('OwnerAliUid')

        if m.get('OwnerEndUserId') is not None:
            self.owner_end_user_id = m.get('OwnerEndUserId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceProperties') is not None:
            self.resource_properties = m.get('ResourceProperties')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

