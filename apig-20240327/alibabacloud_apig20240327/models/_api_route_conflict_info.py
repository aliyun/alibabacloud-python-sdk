# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ApiRouteConflictInfo(DaraModel):
    def __init__(
        self,
        conflicts: List[main_models.ApiRouteConflictInfoConflicts] = None,
        domain_info: main_models.ApiRouteConflictInfoDomainInfo = None,
    ):
        self.conflicts = conflicts
        self.domain_info = domain_info

    def validate(self):
        if self.conflicts:
            for v1 in self.conflicts:
                 if v1:
                    v1.validate()
        if self.domain_info:
            self.domain_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conflicts'] = []
        if self.conflicts is not None:
            for k1 in self.conflicts:
                result['conflicts'].append(k1.to_map() if k1 else None)

        if self.domain_info is not None:
            result['domainInfo'] = self.domain_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conflicts = []
        if m.get('conflicts') is not None:
            for k1 in m.get('conflicts'):
                temp_model = main_models.ApiRouteConflictInfoConflicts()
                self.conflicts.append(temp_model.from_map(k1))

        if m.get('domainInfo') is not None:
            temp_model = main_models.ApiRouteConflictInfoDomainInfo()
            self.domain_info = temp_model.from_map(m.get('domainInfo'))

        return self

class ApiRouteConflictInfoDomainInfo(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        name: str = None,
    ):
        self.domain_id = domain_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['domainId'] = self.domain_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domainId') is not None:
            self.domain_id = m.get('domainId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ApiRouteConflictInfoConflicts(DaraModel):
    def __init__(
        self,
        details: List[main_models.ApiRouteConflictInfoConflictsDetails] = None,
        environment_info: main_models.ApiRouteConflictInfoConflictsEnvironmentInfo = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        route_info: main_models.ApiRouteConflictInfoConflictsRouteInfo = None,
    ):
        self.details = details
        self.environment_info = environment_info
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.route_info = route_info

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()
        if self.environment_info:
            self.environment_info.validate()
        if self.route_info:
            self.route_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['details'].append(k1.to_map() if k1 else None)

        if self.environment_info is not None:
            result['environmentInfo'] = self.environment_info.to_map()

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_name is not None:
            result['resourceName'] = self.resource_name

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.route_info is not None:
            result['routeInfo'] = self.route_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('details') is not None:
            for k1 in m.get('details'):
                temp_model = main_models.ApiRouteConflictInfoConflictsDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('environmentInfo') is not None:
            temp_model = main_models.ApiRouteConflictInfoConflictsEnvironmentInfo()
            self.environment_info = temp_model.from_map(m.get('environmentInfo'))

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceName') is not None:
            self.resource_name = m.get('resourceName')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('routeInfo') is not None:
            temp_model = main_models.ApiRouteConflictInfoConflictsRouteInfo()
            self.route_info = temp_model.from_map(m.get('routeInfo'))

        return self

class ApiRouteConflictInfoConflictsRouteInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        route_id: str = None,
    ):
        self.name = name
        self.route_id = route_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.route_id is not None:
            result['routeId'] = self.route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('routeId') is not None:
            self.route_id = m.get('routeId')

        return self

class ApiRouteConflictInfoConflictsEnvironmentInfo(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        name: str = None,
    ):
        self.environment_id = environment_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ApiRouteConflictInfoConflictsDetails(DaraModel):
    def __init__(
        self,
        conflicting_match: main_models.ApiRouteConflictInfoConflictsDetailsConflictingMatch = None,
        detected_match: main_models.ApiRouteConflictInfoConflictsDetailsDetectedMatch = None,
        level: str = None,
    ):
        self.conflicting_match = conflicting_match
        self.detected_match = detected_match
        self.level = level

    def validate(self):
        if self.conflicting_match:
            self.conflicting_match.validate()
        if self.detected_match:
            self.detected_match.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflicting_match is not None:
            result['conflictingMatch'] = self.conflicting_match.to_map()

        if self.detected_match is not None:
            result['detectedMatch'] = self.detected_match.to_map()

        if self.level is not None:
            result['level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conflictingMatch') is not None:
            temp_model = main_models.ApiRouteConflictInfoConflictsDetailsConflictingMatch()
            self.conflicting_match = temp_model.from_map(m.get('conflictingMatch'))

        if m.get('detectedMatch') is not None:
            temp_model = main_models.ApiRouteConflictInfoConflictsDetailsDetectedMatch()
            self.detected_match = temp_model.from_map(m.get('detectedMatch'))

        if m.get('level') is not None:
            self.level = m.get('level')

        return self

class ApiRouteConflictInfoConflictsDetailsDetectedMatch(DaraModel):
    def __init__(
        self,
        match: main_models.HttpRouteMatch = None,
        operation_info: main_models.ApiRouteConflictInfoConflictsDetailsDetectedMatchOperationInfo = None,
    ):
        self.match = match
        self.operation_info = operation_info

    def validate(self):
        if self.match:
            self.match.validate()
        if self.operation_info:
            self.operation_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.operation_info is not None:
            result['operationInfo'] = self.operation_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            temp_model = main_models.HttpRouteMatch()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('operationInfo') is not None:
            temp_model = main_models.ApiRouteConflictInfoConflictsDetailsDetectedMatchOperationInfo()
            self.operation_info = temp_model.from_map(m.get('operationInfo'))

        return self

class ApiRouteConflictInfoConflictsDetailsDetectedMatchOperationInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation_id: str = None,
    ):
        self.name = name
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        return self

class ApiRouteConflictInfoConflictsDetailsConflictingMatch(DaraModel):
    def __init__(
        self,
        match: main_models.HttpRouteMatch = None,
        operation_info: main_models.ApiRouteConflictInfoConflictsDetailsConflictingMatchOperationInfo = None,
    ):
        self.match = match
        self.operation_info = operation_info

    def validate(self):
        if self.match:
            self.match.validate()
        if self.operation_info:
            self.operation_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match is not None:
            result['match'] = self.match.to_map()

        if self.operation_info is not None:
            result['operationInfo'] = self.operation_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('match') is not None:
            temp_model = main_models.HttpRouteMatch()
            self.match = temp_model.from_map(m.get('match'))

        if m.get('operationInfo') is not None:
            temp_model = main_models.ApiRouteConflictInfoConflictsDetailsConflictingMatchOperationInfo()
            self.operation_info = temp_model.from_map(m.get('operationInfo'))

        return self

class ApiRouteConflictInfoConflictsDetailsConflictingMatchOperationInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        operation_id: str = None,
    ):
        self.name = name
        self.operation_id = operation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        return self

