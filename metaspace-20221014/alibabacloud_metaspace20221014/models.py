# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ApplyCoordinationForCoordinatorRequestCoordinationResourceCandidates(TeaModel):
    def __init__(
        self,
        owner_end_user_id: str = None,
        owner_wy_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        self.owner_end_user_id = owner_end_user_id
        self.owner_wy_id = owner_wy_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_region_id = resource_region_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_end_user_id is not None:
            result['OwnerEndUserId'] = self.owner_end_user_id
        if self.owner_wy_id is not None:
            result['OwnerWyId'] = self.owner_wy_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerEndUserId') is not None:
            self.owner_end_user_id = m.get('OwnerEndUserId')
        if m.get('OwnerWyId') is not None:
            self.owner_wy_id = m.get('OwnerWyId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ApplyCoordinationForCoordinatorRequest(TeaModel):
    def __init__(
        self,
        coordination_resource_candidates: List[ApplyCoordinationForCoordinatorRequestCoordinationResourceCandidates] = None,
        initiator_type: str = None,
        uuid: str = None,
    ):
        self.coordination_resource_candidates = coordination_resource_candidates
        # This parameter is required.
        self.initiator_type = initiator_type
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        if self.coordination_resource_candidates:
            for k in self.coordination_resource_candidates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CoordinationResourceCandidates'] = []
        if self.coordination_resource_candidates is not None:
            for k in self.coordination_resource_candidates:
                result['CoordinationResourceCandidates'].append(k.to_map() if k else None)
        if self.initiator_type is not None:
            result['InitiatorType'] = self.initiator_type
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coordination_resource_candidates = []
        if m.get('CoordinationResourceCandidates') is not None:
            for k in m.get('CoordinationResourceCandidates'):
                temp_model = ApplyCoordinationForCoordinatorRequestCoordinationResourceCandidates()
                self.coordination_resource_candidates.append(temp_model.from_map(k))
        if m.get('InitiatorType') is not None:
            self.initiator_type = m.get('InitiatorType')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyCoordinationForCoordinatorResponseBodyCoordinateFlowModels(TeaModel):
    def __init__(
        self,
        co_id: str = None,
        coordinate_status: str = None,
        coordinate_ticket: str = None,
        coordinator_user_id: str = None,
        owner_user_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
    ):
        self.co_id = co_id
        self.coordinate_status = coordinate_status
        self.coordinate_ticket = coordinate_ticket
        self.coordinator_user_id = coordinator_user_id
        self.owner_user_id = owner_user_id
        self.resource_id = resource_id
        self.resource_name = resource_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_id is not None:
            result['CoId'] = self.co_id
        if self.coordinate_status is not None:
            result['CoordinateStatus'] = self.coordinate_status
        if self.coordinate_ticket is not None:
            result['CoordinateTicket'] = self.coordinate_ticket
        if self.coordinator_user_id is not None:
            result['CoordinatorUserId'] = self.coordinator_user_id
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
        if m.get('CoordinatorUserId') is not None:
            self.coordinator_user_id = m.get('CoordinatorUserId')
        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        return self


class ApplyCoordinationForCoordinatorResponseBody(TeaModel):
    def __init__(
        self,
        coordinate_flow_models: List[ApplyCoordinationForCoordinatorResponseBodyCoordinateFlowModels] = None,
        request_id: str = None,
    ):
        self.coordinate_flow_models = coordinate_flow_models
        self.request_id = request_id

    def validate(self):
        if self.coordinate_flow_models:
            for k in self.coordinate_flow_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CoordinateFlowModels'] = []
        if self.coordinate_flow_models is not None:
            for k in self.coordinate_flow_models:
                result['CoordinateFlowModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coordinate_flow_models = []
        if m.get('CoordinateFlowModels') is not None:
            for k in m.get('CoordinateFlowModels'):
                temp_model = ApplyCoordinationForCoordinatorResponseBodyCoordinateFlowModels()
                self.coordinate_flow_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyCoordinationForCoordinatorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyCoordinationForCoordinatorResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyCoordinationForCoordinatorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCoordinationRequest(TeaModel):
    def __init__(
        self,
        co_ids: List[str] = None,
    ):
        self.co_ids = co_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_ids is not None:
            result['CoIds'] = self.co_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoIds') is not None:
            self.co_ids = m.get('CoIds')
        return self


class CancelCoordinationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelCoordinationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelCoordinationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelCoordinationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCoordinationTicketRequest(TeaModel):
    def __init__(
        self,
        co_id: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.co_id = co_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_id is not None:
            result['CoId'] = self.co_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoId') is not None:
            self.co_id = m.get('CoId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetCoordinationTicketResponseBodyCoordinateTicketModel(TeaModel):
    def __init__(
        self,
        co_id: str = None,
        coordinate_ticket: str = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.co_id = co_id
        self.coordinate_ticket = coordinate_ticket
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_id is not None:
            result['CoId'] = self.co_id
        if self.coordinate_ticket is not None:
            result['CoordinateTicket'] = self.coordinate_ticket
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoId') is not None:
            self.co_id = m.get('CoId')
        if m.get('CoordinateTicket') is not None:
            self.coordinate_ticket = m.get('CoordinateTicket')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetCoordinationTicketResponseBody(TeaModel):
    def __init__(
        self,
        coordinate_ticket_model: GetCoordinationTicketResponseBodyCoordinateTicketModel = None,
        request_id: str = None,
    ):
        self.coordinate_ticket_model = coordinate_ticket_model
        self.request_id = request_id

    def validate(self):
        if self.coordinate_ticket_model:
            self.coordinate_ticket_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coordinate_ticket_model is not None:
            result['CoordinateTicketModel'] = self.coordinate_ticket_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinateTicketModel') is not None:
            temp_model = GetCoordinationTicketResponseBodyCoordinateTicketModel()
            self.coordinate_ticket_model = temp_model.from_map(m['CoordinateTicketModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCoordinationTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCoordinationTicketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCoordinationTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


