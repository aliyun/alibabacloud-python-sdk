# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ApplyCoordinationForMonitoringResponseBody(DaraModel):
    def __init__(
        self,
        coordinate_flow_models: List[main_models.ApplyCoordinationForMonitoringResponseBodyCoordinateFlowModels] = None,
        request_id: str = None,
    ):
        # The list of stream collaboration models.
        self.coordinate_flow_models = coordinate_flow_models
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.coordinate_flow_models:
            for v1 in self.coordinate_flow_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CoordinateFlowModels'] = []
        if self.coordinate_flow_models is not None:
            for k1 in self.coordinate_flow_models:
                result['CoordinateFlowModels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coordinate_flow_models = []
        if m.get('CoordinateFlowModels') is not None:
            for k1 in m.get('CoordinateFlowModels'):
                temp_model = main_models.ApplyCoordinationForMonitoringResponseBodyCoordinateFlowModels()
                self.coordinate_flow_models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ApplyCoordinationForMonitoringResponseBodyCoordinateFlowModels(DaraModel):
    def __init__(
        self,
        co_id: str = None,
        coordinate_status: str = None,
        coordinate_ticket: str = None,
        initiator_type: str = None,
        owner_user_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        # The ID of the stream collaboration.
        self.co_id = co_id
        # The current status of the collaboration task.
        # 
        # Valid values:
        # 
        # *   COORDINATING: The collaboration task is being executed.
        # 
        # *   TERMINATING: The collaboration task is being terminated.
        # 
        # *   TERMINATED: The collaboration task is terminated.
        # 
        # *   PENDING: The collaboration task is pending to be executed.
        self.coordinate_status = coordinate_status
        # The ticket that is used to establish the Adaptive Streaming Protocol (ASP)-based connection.
        self.coordinate_ticket = coordinate_ticket
        # The type of the initiator.
        # 
        # Valid values:
        # 
        # *   ADMIN_INITIATE_FORCE: The administrator forcibly initiates the collaboration request.
        # 
        # *   ADMIN_INITIATE: The administrator initiates the collaboration request.
        # 
        # *   COORDINATOR_INITIATE_FORCE: The coordinator forcibly initiates the collaboration request.
        self.initiator_type = initiator_type
        # The ID of the Alibaba Cloud account of the end user.
        self.owner_user_id = owner_user_id
        # The ID of the cloud desktop.
        self.resource_id = resource_id
        # The name of the cloud desktop.
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.co_id is not None:
            result['CoId'] = self.co_id

        if self.coordinate_status is not None:
            result['CoordinateStatus'] = self.coordinate_status

        if self.coordinate_ticket is not None:
            result['CoordinateTicket'] = self.coordinate_ticket

        if self.initiator_type is not None:
            result['InitiatorType'] = self.initiator_type

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoId') is not None:
            self.co_id = m.get('CoId')

        if m.get('CoordinateStatus') is not None:
            self.coordinate_status = m.get('CoordinateStatus')

        if m.get('CoordinateTicket') is not None:
            self.coordinate_ticket = m.get('CoordinateTicket')

        if m.get('InitiatorType') is not None:
            self.initiator_type = m.get('InitiatorType')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        return self

