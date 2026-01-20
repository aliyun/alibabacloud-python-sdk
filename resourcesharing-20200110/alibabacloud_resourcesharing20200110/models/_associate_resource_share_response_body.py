# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcesharing20200110 import models as main_models
from darabonba.model import DaraModel

class AssociateResourceShareResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share_associations: List[main_models.AssociateResourceShareResponseBodyResourceShareAssociations] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the entities that are associated with the resource share.
        self.resource_share_associations = resource_share_associations

    def validate(self):
        if self.resource_share_associations:
            for v1 in self.resource_share_associations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k1 in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k1 in m.get('ResourceShareAssociations'):
                temp_model = main_models.AssociateResourceShareResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k1))

        return self

class AssociateResourceShareResponseBodyResourceShareAssociations(DaraModel):
    def __init__(
        self,
        association_status: str = None,
        association_status_message: str = None,
        association_type: str = None,
        create_time: str = None,
        entity_id: str = None,
        entity_type: str = None,
        resource_arn: str = None,
        resource_property: str = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
        target_property: str = None,
        update_time: str = None,
    ):
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status = association_status
        # The cause of the association failure.
        self.association_status_message = association_status_message
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        self.association_type = association_type
        # The time when the association of the entity was created. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the shared resource was associated with the resource share.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the principal was associated with the resource share.
        self.create_time = create_time
        # The ID of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the ID of the shared resource.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the ID of the principal.
        self.entity_id = entity_id
        # The type of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of AssociationType is Resource, the value of this parameter is the type of the shared resource. For information about the types of resources that can be shared, see [Services that work with Resource Sharing](https://help.aliyun.com/document_detail/450526.html).
        # *   If the value of AssociationType is Target, the value of this parameter is `Account`.
        self.entity_type = entity_type
        self.resource_arn = resource_arn
        self.resource_property = resource_property
        # The ID of the resource share.
        self.resource_share_id = resource_share_id
        # The name of the resource share.
        self.resource_share_name = resource_share_name
        # The properties of the principal, such as the time range within which the resource is shared.
        # 
        # >  This parameter is returned only if the principal is an Alibaba Cloud service.
        self.target_property = target_property
        # The time when the association of the entity was updated. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the association of the shared resource was updated.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the association of the principal was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status

        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message

        if self.association_type is not None:
            result['AssociationType'] = self.association_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_property is not None:
            result['ResourceProperty'] = self.resource_property

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name

        if self.target_property is not None:
            result['TargetProperty'] = self.target_property

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')

        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')

        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceProperty') is not None:
            self.resource_property = m.get('ResourceProperty')

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')

        if m.get('TargetProperty') is not None:
            self.target_property = m.get('TargetProperty')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

