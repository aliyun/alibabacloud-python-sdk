# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListRolesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListRolesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListRolesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListRolesResponseBodyData(DaraModel):
    def __init__(
        self,
        roles: List[main_models.ListRolesResponseBodyDataRoles] = None,
    ):
        # The MaxCompute project-level roles.
        self.roles = roles

    def validate(self):
        if self.roles:
            for v1 in self.roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['roles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.roles = []
        if m.get('roles') is not None:
            for k1 in m.get('roles'):
                temp_model = main_models.ListRolesResponseBodyDataRoles()
                self.roles.append(temp_model.from_map(k1))

        return self

class ListRolesResponseBodyDataRoles(DaraModel):
    def __init__(
        self,
        acl: main_models.ListRolesResponseBodyDataRolesAcl = None,
        name: str = None,
        policy: str = None,
        type: str = None,
    ):
        # The ACL-based permissions that are granted to the role.
        self.acl = acl
        # The name of the role.
        self.name = name
        # The policy that is attached to the role.
        self.policy = policy
        # The type of the role.
        self.type = type

    def validate(self):
        if self.acl:
            self.acl.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['acl'] = self.acl.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.policy is not None:
            result['policy'] = self.policy

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            temp_model = main_models.ListRolesResponseBodyDataRolesAcl()
            self.acl = temp_model.from_map(m.get('acl'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('policy') is not None:
            self.policy = m.get('policy')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListRolesResponseBodyDataRolesAcl(DaraModel):
    def __init__(
        self,
        function: List[main_models.ListRolesResponseBodyDataRolesAclFunction] = None,
        instance: List[main_models.ListRolesResponseBodyDataRolesAclInstance] = None,
        package: List[main_models.ListRolesResponseBodyDataRolesAclPackage] = None,
        project: List[main_models.ListRolesResponseBodyDataRolesAclProject] = None,
        resource: List[main_models.ListRolesResponseBodyDataRolesAclResource] = None,
        table: List[main_models.ListRolesResponseBodyDataRolesAclTable] = None,
    ):
        # The function.
        self.function = function
        # The instance.
        self.instance = instance
        # The package.
        self.package = package
        # The project.
        self.project = project
        # The resource.
        self.resource = resource
        # The table.
        self.table = table

    def validate(self):
        if self.function:
            for v1 in self.function:
                 if v1:
                    v1.validate()
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()
        if self.package:
            for v1 in self.package:
                 if v1:
                    v1.validate()
        if self.project:
            for v1 in self.project:
                 if v1:
                    v1.validate()
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()
        if self.table:
            for v1 in self.table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['function'] = []
        if self.function is not None:
            for k1 in self.function:
                result['function'].append(k1.to_map() if k1 else None)

        result['instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['instance'].append(k1.to_map() if k1 else None)

        result['package'] = []
        if self.package is not None:
            for k1 in self.package:
                result['package'].append(k1.to_map() if k1 else None)

        result['project'] = []
        if self.project is not None:
            for k1 in self.project:
                result['project'].append(k1.to_map() if k1 else None)

        result['resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['resource'].append(k1.to_map() if k1 else None)

        result['table'] = []
        if self.table is not None:
            for k1 in self.table:
                result['table'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.function = []
        if m.get('function') is not None:
            for k1 in m.get('function'):
                temp_model = main_models.ListRolesResponseBodyDataRolesAclFunction()
                self.function.append(temp_model.from_map(k1))

        self.instance = []
        if m.get('instance') is not None:
            for k1 in m.get('instance'):
                temp_model = main_models.ListRolesResponseBodyDataRolesAclInstance()
                self.instance.append(temp_model.from_map(k1))

        self.package = []
        if m.get('package') is not None:
            for k1 in m.get('package'):
                temp_model = main_models.ListRolesResponseBodyDataRolesAclPackage()
                self.package.append(temp_model.from_map(k1))

        self.project = []
        if m.get('project') is not None:
            for k1 in m.get('project'):
                temp_model = main_models.ListRolesResponseBodyDataRolesAclProject()
                self.project.append(temp_model.from_map(k1))

        self.resource = []
        if m.get('resource') is not None:
            for k1 in m.get('resource'):
                temp_model = main_models.ListRolesResponseBodyDataRolesAclResource()
                self.resource.append(temp_model.from_map(k1))

        self.table = []
        if m.get('table') is not None:
            for k1 in m.get('table'):
                temp_model = main_models.ListRolesResponseBodyDataRolesAclTable()
                self.table.append(temp_model.from_map(k1))

        return self

class ListRolesResponseBodyDataRolesAclTable(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the table.
        self.actions = actions
        # The name of the table.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListRolesResponseBodyDataRolesAclResource(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the resource.
        self.actions = actions
        # The name of the resource.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListRolesResponseBodyDataRolesAclProject(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the project.
        self.actions = actions
        # The name of the MaxCompute project.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListRolesResponseBodyDataRolesAclPackage(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the package.
        self.actions = actions
        # The name of the package.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListRolesResponseBodyDataRolesAclInstance(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the instance.
        self.actions = actions
        # The name of the instance.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListRolesResponseBodyDataRolesAclFunction(DaraModel):
    def __init__(
        self,
        actions: List[str] = None,
        name: str = None,
    ):
        # The operations that were performed on the function.
        self.actions = actions
        # The name of the function.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actions is not None:
            result['actions'] = self.actions

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

