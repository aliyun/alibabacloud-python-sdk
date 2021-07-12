# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DeleteServiceRequest(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        io_tcloud_connector_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.service_id = service_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteServiceResponseBody(TeaModel):
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


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceEntryRequest(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        io_tcloud_connector_id: str = None,
        service_entry_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.service_id = service_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.service_entry_id = service_entry_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteServiceEntryResponseBody(TeaModel):
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


class DeleteServiceEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServiceEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteServiceEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceEntryAttributeRequest(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        io_tcloud_connector_id: str = None,
        service_entry_id: str = None,
        service_entry_name: str = None,
        service_entry_description: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.service_id = service_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.service_entry_id = service_entry_id
        self.service_entry_name = service_entry_name
        self.service_entry_description = service_entry_description
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateServiceEntryAttributeResponseBody(TeaModel):
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


class UpdateServiceEntryAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServiceEntryAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateServiceEntryAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceAttributeRequest(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        io_tcloud_connector_id: str = None,
        service_name: str = None,
        service_description: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.service_id = service_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.service_name = service_name
        self.service_description = service_description
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateServiceAttributeResponseBody(TeaModel):
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


class UpdateServiceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServiceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateServiceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthorizationRulesRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        authorization_rule_ids: List[str] = None,
        destination_type: List[str] = None,
        authorization_rule_status: List[str] = None,
        authorization_rule_name: List[str] = None,
        policy: List[str] = None,
        next_token: str = None,
        max_results: int = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.authorization_rule_ids = authorization_rule_ids
        self.destination_type = destination_type
        self.authorization_rule_status = authorization_rule_status
        self.authorization_rule_name = authorization_rule_name
        self.policy = policy
        self.next_token = next_token
        self.max_results = max_results
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.authorization_rule_ids is not None:
            result['AuthorizationRuleIds'] = self.authorization_rule_ids
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AuthorizationRuleIds') is not None:
            self.authorization_rule_ids = m.get('AuthorizationRuleIds')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAuthorizationRulesResponseBodyAuthorizationRules(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        policy: str = None,
        authorization_rule_status: str = None,
        source_cidrs: List[str] = None,
        destination_type: str = None,
        destination: str = None,
        authorization_rule_name: str = None,
        authorization_rule_description: str = None,
        authorization_rule_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.policy = policy
        self.authorization_rule_status = authorization_rule_status
        self.source_cidrs = source_cidrs
        self.destination_type = destination_type
        self.destination = destination
        self.authorization_rule_name = authorization_rule_name
        self.authorization_rule_description = authorization_rule_description
        self.authorization_rule_id = authorization_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.authorization_rule_status is not None:
            result['AuthorizationRuleStatus'] = self.authorization_rule_status
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('AuthorizationRuleStatus') is not None:
            self.authorization_rule_status = m.get('AuthorizationRuleStatus')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        return self


class ListAuthorizationRulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        next_token: str = None,
        max_results: int = None,
        authorization_rules: List[ListAuthorizationRulesResponseBodyAuthorizationRules] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.next_token = next_token
        self.max_results = max_results
        self.authorization_rules = authorization_rules

    def validate(self):
        if self.authorization_rules:
            for k in self.authorization_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['AuthorizationRules'] = []
        if self.authorization_rules is not None:
            for k in self.authorization_rules:
                result['AuthorizationRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.authorization_rules = []
        if m.get('AuthorizationRules') is not None:
            for k in m.get('AuthorizationRules'):
                temp_model = ListAuthorizationRulesResponseBodyAuthorizationRules()
                self.authorization_rules.append(temp_model.from_map(k))
        return self


class ListAuthorizationRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAuthorizationRulesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAuthorizationRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        service_ids: List[str] = None,
        service_names: List[str] = None,
        resource_statuses: List[str] = None,
        next_token: str = None,
        max_results: int = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.service_ids = service_ids
        self.service_names = service_names
        self.resource_statuses = resource_statuses
        self.next_token = next_token
        self.max_results = max_results
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_ids is not None:
            result['ServiceIds'] = self.service_ids
        if self.service_names is not None:
            result['ServiceNames'] = self.service_names
        if self.resource_statuses is not None:
            result['ResourceStatuses'] = self.resource_statuses
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceIds') is not None:
            self.service_ids = m.get('ServiceIds')
        if m.get('ServiceNames') is not None:
            self.service_names = m.get('ServiceNames')
        if m.get('ResourceStatuses') is not None:
            self.resource_statuses = m.get('ResourceStatuses')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListServiceResponseBodyServices(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        service_id: str = None,
        service_status: str = None,
        service_name: str = None,
        service_description: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.service_id = service_id
        self.service_status = service_status
        self.service_name = service_name
        self.service_description = service_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        return self


class ListServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        next_token: str = None,
        max_results: int = None,
        services: List[ListServiceResponseBodyServices] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.next_token = next_token
        self.max_results = max_results
        self.services = services

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServiceResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        return self


class ListServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateVSwitchWithIoTCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        vpc_id: str = None,
        v_switch_list: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.vpc_id = vpc_id
        self.v_switch_list = v_switch_list
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_list is not None:
            result['VSwitchList'] = self.v_switch_list
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchList') is not None:
            self.v_switch_list = m.get('VSwitchList')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateVSwitchWithIoTCloudConnectorResponseBody(TeaModel):
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


class AssociateVSwitchWithIoTCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateVSwitchWithIoTCloudConnectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociateVSwitchWithIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConnectionPoolsRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        connection_pool_ids: List[str] = None,
        connection_pool_name: List[str] = None,
        connection_pool_status: List[str] = None,
        next_token: str = None,
        max_results: int = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.connection_pool_ids = connection_pool_ids
        self.connection_pool_name = connection_pool_name
        self.connection_pool_status = connection_pool_status
        self.next_token = next_token
        self.max_results = max_results
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.connection_pool_ids is not None:
            result['ConnectionPoolIds'] = self.connection_pool_ids
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_status is not None:
            result['ConnectionPoolStatus'] = self.connection_pool_status
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ConnectionPoolIds') is not None:
            self.connection_pool_ids = m.get('ConnectionPoolIds')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolStatus') is not None:
            self.connection_pool_status = m.get('ConnectionPoolStatus')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListConnectionPoolsResponseBodyConnectionPools(TeaModel):
    def __init__(
        self,
        connection_pool_id: str = None,
        connection_pool_status: str = None,
        connection_pool_name: str = None,
        connection_pool_description: str = None,
        cidrs: List[str] = None,
    ):
        self.connection_pool_id = connection_pool_id
        self.connection_pool_status = connection_pool_status
        self.connection_pool_name = connection_pool_name
        self.connection_pool_description = connection_pool_description
        self.cidrs = cidrs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.connection_pool_status is not None:
            result['ConnectionPoolStatus'] = self.connection_pool_status
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('ConnectionPoolStatus') is not None:
            self.connection_pool_status = m.get('ConnectionPoolStatus')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        return self


class ListConnectionPoolsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        next_token: str = None,
        max_results: int = None,
        connection_pools: List[ListConnectionPoolsResponseBodyConnectionPools] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.next_token = next_token
        self.max_results = max_results
        self.connection_pools = connection_pools

    def validate(self):
        if self.connection_pools:
            for k in self.connection_pools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ConnectionPools'] = []
        if self.connection_pools is not None:
            for k in self.connection_pools:
                result['ConnectionPools'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.connection_pools = []
        if m.get('ConnectionPools') is not None:
            for k in m.get('ConnectionPools'):
                temp_model = ListConnectionPoolsResponseBodyConnectionPools()
                self.connection_pools.append(temp_model.from_map(k))
        return self


class ListConnectionPoolsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConnectionPoolsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListConnectionPoolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnectionPoolAttributeRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        connection_pool_id: str = None,
        count: int = None,
        connection_pool_name: str = None,
        connection_pool_description: str = None,
        cidrs: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.connection_pool_id = connection_pool_id
        self.count = count
        self.connection_pool_name = connection_pool_name
        self.connection_pool_description = connection_pool_description
        self.cidrs = cidrs
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.count is not None:
            result['Count'] = self.count
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateConnectionPoolAttributeResponseBody(TeaModel):
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


class UpdateConnectionPoolAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConnectionPoolAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateConnectionPoolAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableIoTCloudConnectorAccessLogResponseBody(TeaModel):
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


class DisableIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisableIoTCloudConnectorAccessLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConnectionPoolRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        count: int = None,
        connection_pool_name: str = None,
        connection_pool_description: str = None,
        cidrs: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.count = count
        self.connection_pool_name = connection_pool_name
        self.connection_pool_description = connection_pool_description
        self.cidrs = cidrs
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.count is not None:
            result['Count'] = self.count
        if self.connection_pool_name is not None:
            result['ConnectionPoolName'] = self.connection_pool_name
        if self.connection_pool_description is not None:
            result['ConnectionPoolDescription'] = self.connection_pool_description
        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('ConnectionPoolName') is not None:
            self.connection_pool_name = m.get('ConnectionPoolName')
        if m.get('ConnectionPoolDescription') is not None:
            self.connection_pool_description = m.get('ConnectionPoolDescription')
        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateConnectionPoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        connection_pool_id: str = None,
    ):
        self.request_id = request_id
        self.connection_pool_id = connection_pool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        return self


class CreateConnectionPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConnectionPoolResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        destination_type: str = None,
        destination: str = None,
        policy: str = None,
        source_cidrs: List[str] = None,
        authorization_rule_name: str = None,
        authorization_rule_description: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.destination_type = destination_type
        self.destination = destination
        self.policy = policy
        self.source_cidrs = source_cidrs
        self.authorization_rule_name = authorization_rule_name
        self.authorization_rule_description = authorization_rule_description
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateAuthorizationRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        authorization_rule_id: str = None,
    ):
        self.request_id = request_id
        self.authorization_rule_id = authorization_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        return self


class CreateAuthorizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAuthorizationRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIoTCloudConnectorAttributeRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        io_tcloud_connector_name: str = None,
        io_tcloud_connector_description: str = None,
        wildcard_domain_enabled: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.io_tcloud_connector_name = io_tcloud_connector_name
        self.io_tcloud_connector_description = io_tcloud_connector_description
        self.wildcard_domain_enabled = wildcard_domain_enabled
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateIoTCloudConnectorAttributeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_id: str = None,
    ):
        self.request_id = request_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class UpdateIoTCloudConnectorAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateIoTCloudConnectorAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateIoTCloudConnectorAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIoTCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteIoTCloudConnectorResponseBody(TeaModel):
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


class DeleteIoTCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIoTCloudConnectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorAvailableZonesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        io_tcloud_connector_id: str = None,
    ):
        self.region_id = region_id
        self.io_tcloud_connector_id = io_tcloud_connector_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        return self


class ListIoTCloudConnectorAvailableZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        io_tcloud_connector_id: str = None,
        available_zone_list: List[str] = None,
    ):
        self.request_id = request_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.available_zone_list = available_zone_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.available_zone_list is not None:
            result['AvailableZoneList'] = self.available_zone_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AvailableZoneList') is not None:
            self.available_zone_list = m.get('AvailableZoneList')
        return self


class ListIoTCloudConnectorAvailableZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIoTCloudConnectorAvailableZonesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIoTCloudConnectorAvailableZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetIoTCloudConnectorAccessLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_log_sls_project: str = None,
        access_log_sls_log_store: str = None,
        access_log_status: str = None,
    ):
        self.request_id = request_id
        self.access_log_sls_project = access_log_sls_project
        self.access_log_sls_log_store = access_log_sls_log_store
        self.access_log_status = access_log_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_log_sls_project is not None:
            result['AccessLogSlsProject'] = self.access_log_sls_project
        if self.access_log_sls_log_store is not None:
            result['AccessLogSlsLogStore'] = self.access_log_sls_log_store
        if self.access_log_status is not None:
            result['AccessLogStatus'] = self.access_log_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessLogSlsProject') is not None:
            self.access_log_sls_project = m.get('AccessLogSlsProject')
        if m.get('AccessLogSlsLogStore') is not None:
            self.access_log_sls_log_store = m.get('AccessLogSlsLogStore')
        if m.get('AccessLogStatus') is not None:
            self.access_log_status = m.get('AccessLogStatus')
        return self


class GetIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetIoTCloudConnectorAccessLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthorizationRuleRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        authorization_rule_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.authorization_rule_id = authorization_rule_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAuthorizationRuleResponseBody(TeaModel):
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


class DeleteAuthorizationRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAuthorizationRuleResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAuthorizationRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConnectionPoolRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        connection_pool_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.connection_pool_id = connection_pool_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.connection_pool_id is not None:
            result['ConnectionPoolId'] = self.connection_pool_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ConnectionPoolId') is not None:
            self.connection_pool_id = m.get('ConnectionPoolId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteConnectionPoolResponseBody(TeaModel):
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


class DeleteConnectionPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConnectionPoolResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteConnectionPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateVSwitchFromIoTCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DissociateVSwitchFromIoTCloudConnectorResponseBody(TeaModel):
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


class DissociateVSwitchFromIoTCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DissociateVSwitchFromIoTCloudConnectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DissociateVSwitchFromIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableIoTCloudConnectorAccessLogRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        access_log_sls_project: str = None,
        access_log_sls_log_store: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.access_log_sls_project = access_log_sls_project
        self.access_log_sls_log_store = access_log_sls_log_store
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.access_log_sls_project is not None:
            result['AccessLogSlsProject'] = self.access_log_sls_project
        if self.access_log_sls_log_store is not None:
            result['AccessLogSlsLogStore'] = self.access_log_sls_log_store
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AccessLogSlsProject') is not None:
            self.access_log_sls_project = m.get('AccessLogSlsProject')
        if m.get('AccessLogSlsLogStore') is not None:
            self.access_log_sls_log_store = m.get('AccessLogSlsLogStore')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableIoTCloudConnectorAccessLogResponseBody(TeaModel):
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


class EnableIoTCloudConnectorAccessLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableIoTCloudConnectorAccessLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableIoTCloudConnectorAccessLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceEntriesRequest(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        io_tcloud_connector_id: str = None,
        target: List[str] = None,
        target_type: List[str] = None,
        service_entry_status: List[str] = None,
        service_entry_name: List[str] = None,
        next_token: str = None,
        max_results: int = None,
        region_id: str = None,
        service_entry_ids: List[str] = None,
    ):
        self.service_id = service_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.target = target
        self.target_type = target_type
        self.service_entry_status = service_entry_status
        self.service_entry_name = service_entry_name
        self.next_token = next_token
        self.max_results = max_results
        self.region_id = region_id
        self.service_entry_ids = service_entry_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.service_entry_status is not None:
            result['ServiceEntryStatus'] = self.service_entry_status
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_entry_ids is not None:
            result['ServiceEntryIds'] = self.service_entry_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ServiceEntryStatus') is not None:
            self.service_entry_status = m.get('ServiceEntryStatus')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceEntryIds') is not None:
            self.service_entry_ids = m.get('ServiceEntryIds')
        return self


class ListServiceEntriesResponseBodyServiceEntries(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        service_entry_status: str = None,
        target: str = None,
        target_type: str = None,
        service_entry_name: str = None,
        service_entry_description: str = None,
        service_entry_id: str = None,
    ):
        self.service_id = service_id
        self.service_entry_status = service_entry_status
        self.target = target
        self.target_type = target_type
        self.service_entry_name = service_entry_name
        self.service_entry_description = service_entry_description
        self.service_entry_id = service_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_entry_status is not None:
            result['ServiceEntryStatus'] = self.service_entry_status
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceEntryStatus') is not None:
            self.service_entry_status = m.get('ServiceEntryStatus')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        return self


class ListServiceEntriesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        next_token: str = None,
        max_results: int = None,
        service_entries: List[ListServiceEntriesResponseBodyServiceEntries] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.next_token = next_token
        self.max_results = max_results
        self.service_entries = service_entries

    def validate(self):
        if self.service_entries:
            for k in self.service_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['ServiceEntries'] = []
        if self.service_entries is not None:
            for k in self.service_entries:
                result['ServiceEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.service_entries = []
        if m.get('ServiceEntries') is not None:
            for k in m.get('ServiceEntries'):
                temp_model = ListServiceEntriesResponseBodyServiceEntries()
                self.service_entries.append(temp_model.from_map(k))
        return self


class ListServiceEntriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListServiceEntriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListServiceEntriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        service_name: str = None,
        service_description: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.service_name = service_name
        self.service_description = service_description
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_id: str = None,
    ):
        self.request_id = request_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIoTCloudConnectorsRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_status: List[str] = None,
        io_tcloud_connector_ids: List[str] = None,
        io_tcloud_connector_name: List[str] = None,
        isps: List[str] = None,
        vpc_ids: List[str] = None,
        apns: List[str] = None,
        next_token: str = None,
        max_results: int = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_status = io_tcloud_connector_status
        self.io_tcloud_connector_ids = io_tcloud_connector_ids
        self.io_tcloud_connector_name = io_tcloud_connector_name
        self.isps = isps
        self.vpc_ids = vpc_ids
        self.apns = apns
        self.next_token = next_token
        self.max_results = max_results
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        if self.io_tcloud_connector_ids is not None:
            result['IoTCloudConnectorIds'] = self.io_tcloud_connector_ids
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.isps is not None:
            result['Isps'] = self.isps
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.apns is not None:
            result['Apns'] = self.apns
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        if m.get('IoTCloudConnectorIds') is not None:
            self.io_tcloud_connector_ids = m.get('IoTCloudConnectorIds')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('Isps') is not None:
            self.isps = m.get('Isps')
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('Apns') is not None:
            self.apns = m.get('Apns')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListIoTCloudConnectorsResponseBodyIoTCloudConnectors(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        io_tcloud_connector_status: str = None,
        isp: str = None,
        io_tcloud_connector_business_status: str = None,
        apn: str = None,
        rate_limit: int = None,
        vpc_id: str = None,
        v_switch_ids: List[str] = None,
        io_tcloud_connector_name: str = None,
        io_tcloud_connector_description: str = None,
        wildcard_domain_enabled: bool = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.io_tcloud_connector_status = io_tcloud_connector_status
        self.isp = isp
        self.io_tcloud_connector_business_status = io_tcloud_connector_business_status
        self.apn = apn
        self.rate_limit = rate_limit
        self.vpc_id = vpc_id
        self.v_switch_ids = v_switch_ids
        self.io_tcloud_connector_name = io_tcloud_connector_name
        self.io_tcloud_connector_description = io_tcloud_connector_description
        self.wildcard_domain_enabled = wildcard_domain_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.io_tcloud_connector_status is not None:
            result['IoTCloudConnectorStatus'] = self.io_tcloud_connector_status
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.io_tcloud_connector_business_status is not None:
            result['IoTCloudConnectorBusinessStatus'] = self.io_tcloud_connector_business_status
        if self.apn is not None:
            result['Apn'] = self.apn
        if self.rate_limit is not None:
            result['RateLimit'] = self.rate_limit
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('IoTCloudConnectorStatus') is not None:
            self.io_tcloud_connector_status = m.get('IoTCloudConnectorStatus')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('IoTCloudConnectorBusinessStatus') is not None:
            self.io_tcloud_connector_business_status = m.get('IoTCloudConnectorBusinessStatus')
        if m.get('Apn') is not None:
            self.apn = m.get('Apn')
        if m.get('RateLimit') is not None:
            self.rate_limit = m.get('RateLimit')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        return self


class ListIoTCloudConnectorsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        next_token: str = None,
        max_results: int = None,
        request_id: str = None,
        io_tcloud_connectors: List[ListIoTCloudConnectorsResponseBodyIoTCloudConnectors] = None,
    ):
        self.total_count = total_count
        self.next_token = next_token
        self.max_results = max_results
        self.request_id = request_id
        self.io_tcloud_connectors = io_tcloud_connectors

    def validate(self):
        if self.io_tcloud_connectors:
            for k in self.io_tcloud_connectors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['IoTCloudConnectors'] = []
        if self.io_tcloud_connectors is not None:
            for k in self.io_tcloud_connectors:
                result['IoTCloudConnectors'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.io_tcloud_connectors = []
        if m.get('IoTCloudConnectors') is not None:
            for k in m.get('IoTCloudConnectors'):
                temp_model = ListIoTCloudConnectorsResponseBodyIoTCloudConnectors()
                self.io_tcloud_connectors.append(temp_model.from_map(k))
        return self


class ListIoTCloudConnectorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIoTCloudConnectorsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIoTCloudConnectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIoTCloudConnectorRequest(TeaModel):
    def __init__(
        self,
        isp: str = None,
        apn: str = None,
        io_tcloud_connector_name: str = None,
        io_tcloud_connector_description: str = None,
        wildcard_domain_enabled: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.isp = isp
        self.apn = apn
        self.io_tcloud_connector_name = io_tcloud_connector_name
        self.io_tcloud_connector_description = io_tcloud_connector_description
        self.wildcard_domain_enabled = wildcard_domain_enabled
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isp is not None:
            result['ISP'] = self.isp
        if self.apn is not None:
            result['APN'] = self.apn
        if self.io_tcloud_connector_name is not None:
            result['IoTCloudConnectorName'] = self.io_tcloud_connector_name
        if self.io_tcloud_connector_description is not None:
            result['IoTCloudConnectorDescription'] = self.io_tcloud_connector_description
        if self.wildcard_domain_enabled is not None:
            result['WildcardDomainEnabled'] = self.wildcard_domain_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ISP') is not None:
            self.isp = m.get('ISP')
        if m.get('APN') is not None:
            self.apn = m.get('APN')
        if m.get('IoTCloudConnectorName') is not None:
            self.io_tcloud_connector_name = m.get('IoTCloudConnectorName')
        if m.get('IoTCloudConnectorDescription') is not None:
            self.io_tcloud_connector_description = m.get('IoTCloudConnectorDescription')
        if m.get('WildcardDomainEnabled') is not None:
            self.wildcard_domain_enabled = m.get('WildcardDomainEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateIoTCloudConnectorResponseBody(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        request_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateIoTCloudConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIoTCloudConnectorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIoTCloudConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuthorizationRuleAttributeRequest(TeaModel):
    def __init__(
        self,
        io_tcloud_connector_id: str = None,
        authorization_rule_id: str = None,
        destination_type: str = None,
        destination: str = None,
        policy: str = None,
        source_cidrs: List[str] = None,
        authorization_rule_name: str = None,
        authorization_rule_description: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.authorization_rule_id = authorization_rule_id
        self.destination_type = destination_type
        self.destination = destination
        self.policy = policy
        self.source_cidrs = source_cidrs
        self.authorization_rule_name = authorization_rule_name
        self.authorization_rule_description = authorization_rule_description
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.authorization_rule_id is not None:
            result['AuthorizationRuleId'] = self.authorization_rule_id
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.source_cidrs is not None:
            result['SourceCidrs'] = self.source_cidrs
        if self.authorization_rule_name is not None:
            result['AuthorizationRuleName'] = self.authorization_rule_name
        if self.authorization_rule_description is not None:
            result['AuthorizationRuleDescription'] = self.authorization_rule_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('AuthorizationRuleId') is not None:
            self.authorization_rule_id = m.get('AuthorizationRuleId')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SourceCidrs') is not None:
            self.source_cidrs = m.get('SourceCidrs')
        if m.get('AuthorizationRuleName') is not None:
            self.authorization_rule_name = m.get('AuthorizationRuleName')
        if m.get('AuthorizationRuleDescription') is not None:
            self.authorization_rule_description = m.get('AuthorizationRuleDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateAuthorizationRuleAttributeResponseBody(TeaModel):
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


class UpdateAuthorizationRuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAuthorizationRuleAttributeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateAuthorizationRuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceEntryRequest(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        io_tcloud_connector_id: str = None,
        target: str = None,
        target_type: str = None,
        service_entry_name: str = None,
        service_entry_description: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
    ):
        self.service_id = service_id
        self.io_tcloud_connector_id = io_tcloud_connector_id
        self.target = target
        self.target_type = target_type
        self.service_entry_name = service_entry_name
        self.service_entry_description = service_entry_description
        self.client_token = client_token
        self.dry_run = dry_run
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.io_tcloud_connector_id is not None:
            result['IoTCloudConnectorId'] = self.io_tcloud_connector_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.service_entry_name is not None:
            result['ServiceEntryName'] = self.service_entry_name
        if self.service_entry_description is not None:
            result['ServiceEntryDescription'] = self.service_entry_description
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('IoTCloudConnectorId') is not None:
            self.io_tcloud_connector_id = m.get('IoTCloudConnectorId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('ServiceEntryName') is not None:
            self.service_entry_name = m.get('ServiceEntryName')
        if m.get('ServiceEntryDescription') is not None:
            self.service_entry_description = m.get('ServiceEntryDescription')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateServiceEntryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_entry_id: str = None,
    ):
        self.request_id = request_id
        self.service_entry_id = service_entry_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_entry_id is not None:
            result['ServiceEntryId'] = self.service_entry_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceEntryId') is not None:
            self.service_entry_id = m.get('ServiceEntryId')
        return self


class CreateServiceEntryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceEntryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateServiceEntryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


