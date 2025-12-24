# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityGroupReferencesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_group_references: main_models.DescribeSecurityGroupReferencesResponseBodySecurityGroupReferences = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # Details about the references to the specified security groups.
        self.security_group_references = security_group_references

    def validate(self):
        if self.security_group_references:
            self.security_group_references.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group_references is not None:
            result['SecurityGroupReferences'] = self.security_group_references.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroupReferences') is not None:
            temp_model = main_models.DescribeSecurityGroupReferencesResponseBodySecurityGroupReferences()
            self.security_group_references = temp_model.from_map(m.get('SecurityGroupReferences'))

        return self

class DescribeSecurityGroupReferencesResponseBodySecurityGroupReferences(DaraModel):
    def __init__(
        self,
        security_group_reference: List[main_models.DescribeSecurityGroupReferencesResponseBodySecurityGroupReferencesSecurityGroupReference] = None,
    ):
        self.security_group_reference = security_group_reference

    def validate(self):
        if self.security_group_reference:
            for v1 in self.security_group_reference:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SecurityGroupReference'] = []
        if self.security_group_reference is not None:
            for k1 in self.security_group_reference:
                result['SecurityGroupReference'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.security_group_reference = []
        if m.get('SecurityGroupReference') is not None:
            for k1 in m.get('SecurityGroupReference'):
                temp_model = main_models.DescribeSecurityGroupReferencesResponseBodySecurityGroupReferencesSecurityGroupReference()
                self.security_group_reference.append(temp_model.from_map(k1))

        return self

class DescribeSecurityGroupReferencesResponseBodySecurityGroupReferencesSecurityGroupReference(DaraModel):
    def __init__(
        self,
        referencing_security_groups: main_models.DescribeSecurityGroupReferencesResponseBodySecurityGroupReferencesSecurityGroupReferenceReferencingSecurityGroups = None,
        security_group_id: str = None,
    ):
        # Details about the security groups whose rules reference the specified security group.
        self.referencing_security_groups = referencing_security_groups
        # The ID of the specified security group.
        self.security_group_id = security_group_id

    def validate(self):
        if self.referencing_security_groups:
            self.referencing_security_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.referencing_security_groups is not None:
            result['ReferencingSecurityGroups'] = self.referencing_security_groups.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferencingSecurityGroups') is not None:
            temp_model = main_models.DescribeSecurityGroupReferencesResponseBodySecurityGroupReferencesSecurityGroupReferenceReferencingSecurityGroups()
            self.referencing_security_groups = temp_model.from_map(m.get('ReferencingSecurityGroups'))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

class DescribeSecurityGroupReferencesResponseBodySecurityGroupReferencesSecurityGroupReferenceReferencingSecurityGroups(DaraModel):
    def __init__(
        self,
        referencing_security_group: List[main_models.DescribeSecurityGroupReferencesResponseBodySecurityGroupReferencesSecurityGroupReferenceReferencingSecurityGroupsReferencingSecurityGroup] = None,
    ):
        self.referencing_security_group = referencing_security_group

    def validate(self):
        if self.referencing_security_group:
            for v1 in self.referencing_security_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReferencingSecurityGroup'] = []
        if self.referencing_security_group is not None:
            for k1 in self.referencing_security_group:
                result['ReferencingSecurityGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.referencing_security_group = []
        if m.get('ReferencingSecurityGroup') is not None:
            for k1 in m.get('ReferencingSecurityGroup'):
                temp_model = main_models.DescribeSecurityGroupReferencesResponseBodySecurityGroupReferencesSecurityGroupReferenceReferencingSecurityGroupsReferencingSecurityGroup()
                self.referencing_security_group.append(temp_model.from_map(k1))

        return self

class DescribeSecurityGroupReferencesResponseBodySecurityGroupReferencesSecurityGroupReferenceReferencingSecurityGroupsReferencingSecurityGroup(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        security_group_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the security group whose rules reference the specified security group belongs.
        self.ali_uid = ali_uid
        # The ID of the security group whose rules reference the specified security group.
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        return self

