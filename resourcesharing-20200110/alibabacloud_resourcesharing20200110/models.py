# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AssociateResourceShareRequestResources(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class AssociateResourceShareRequest(TeaModel):
    def __init__(
        self,
        resource_share_id: str = None,
        resources: List[AssociateResourceShareRequestResources] = None,
        targets: List[str] = None,
    ):
        self.resource_share_id = resource_share_id
        self.resources = resources
        self.targets = targets

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = AssociateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class AssociateResourceShareResponseBodyResourceShareAssociations(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        entity_id: str = None,
        resource_share_name: str = None,
        create_time: str = None,
        entity_type: str = None,
        resource_share_id: str = None,
        association_status_message: str = None,
        association_type: str = None,
        association_status: str = None,
    ):
        self.update_time = update_time
        self.entity_id = entity_id
        self.resource_share_name = resource_share_name
        self.create_time = create_time
        self.entity_type = entity_type
        self.resource_share_id = resource_share_id
        self.association_status_message = association_status_message
        self.association_type = association_type
        self.association_status = association_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        return self


class AssociateResourceShareResponseBody(TeaModel):
    def __init__(
        self,
        resource_share_associations: List[AssociateResourceShareResponseBodyResourceShareAssociations] = None,
        request_id: str = None,
    ):
        self.resource_share_associations = resource_share_associations
        self.request_id = request_id

    def validate(self):
        if self.resource_share_associations:
            for k in self.resource_share_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k in m.get('ResourceShareAssociations'):
                temp_model = AssociateResourceShareResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociateResourceShareResponseBody = None,
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
            temp_model = AssociateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceShareRequestResources(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class CreateResourceShareRequest(TeaModel):
    def __init__(
        self,
        resource_share_name: str = None,
        resources: List[CreateResourceShareRequestResources] = None,
        targets: List[str] = None,
    ):
        self.resource_share_name = resource_share_name
        self.resources = resources
        self.targets = targets

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = CreateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class CreateResourceShareResponseBodyResourceShare(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        resource_share_name: str = None,
        resource_share_owner: str = None,
        create_time: str = None,
        resource_share_id: str = None,
        resource_share_status: str = None,
    ):
        self.update_time = update_time
        self.resource_share_name = resource_share_name
        self.resource_share_owner = resource_share_owner
        self.create_time = create_time
        self.resource_share_id = resource_share_id
        self.resource_share_status = resource_share_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        return self


class CreateResourceShareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share: CreateResourceShareResponseBodyResourceShare = None,
    ):
        self.request_id = request_id
        self.resource_share = resource_share

    def validate(self):
        if self.resource_share:
            self.resource_share.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_share is not None:
            result['ResourceShare'] = self.resource_share.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceShare') is not None:
            temp_model = CreateResourceShareResponseBodyResourceShare()
            self.resource_share = temp_model.from_map(m['ResourceShare'])
        return self


class CreateResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateResourceShareResponseBody = None,
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
            temp_model = CreateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceShareRequest(TeaModel):
    def __init__(
        self,
        resource_share_id: str = None,
    ):
        self.resource_share_id = resource_share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        return self


class DeleteResourceShareResponseBody(TeaModel):
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


class DeleteResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteResourceShareResponseBody = None,
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
            temp_model = DeleteResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateResourceShareRequestResources(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        resource_id: str = None,
    ):
        self.resource_type = resource_type
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class DisassociateResourceShareRequest(TeaModel):
    def __init__(
        self,
        resource_share_id: str = None,
        resources: List[DisassociateResourceShareRequestResources] = None,
        targets: List[str] = None,
    ):
        self.resource_share_id = resource_share_id
        self.resources = resources
        self.targets = targets

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = DisassociateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class DisassociateResourceShareResponseBodyResourceShareAssociations(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        entity_id: str = None,
        resource_share_name: str = None,
        create_time: str = None,
        entity_type: str = None,
        resource_share_id: str = None,
        association_status_message: str = None,
        association_type: str = None,
        association_status: str = None,
    ):
        self.update_time = update_time
        self.entity_id = entity_id
        self.resource_share_name = resource_share_name
        self.create_time = create_time
        self.entity_type = entity_type
        self.resource_share_id = resource_share_id
        self.association_status_message = association_status_message
        self.association_type = association_type
        self.association_status = association_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        return self


class DisassociateResourceShareResponseBody(TeaModel):
    def __init__(
        self,
        resource_share_associations: List[DisassociateResourceShareResponseBodyResourceShareAssociations] = None,
        request_id: str = None,
    ):
        self.resource_share_associations = resource_share_associations
        self.request_id = request_id

    def validate(self):
        if self.resource_share_associations:
            for k in self.resource_share_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k in m.get('ResourceShareAssociations'):
                temp_model = DisassociateResourceShareResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DisassociateResourceShareResponseBody = None,
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
            temp_model = DisassociateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceShareAssociationsRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        target: str = None,
        association_type: str = None,
        association_status: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_share_ids: List[str] = None,
    ):
        self.resource_id = resource_id
        self.target = target
        self.association_type = association_type
        self.association_status = association_status
        self.max_results = max_results
        self.next_token = next_token
        self.resource_share_ids = resource_share_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.target is not None:
            result['Target'] = self.target
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        return self


class ListResourceShareAssociationsResponseBodyResourceShareAssociations(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        entity_id: str = None,
        resource_share_name: str = None,
        create_time: str = None,
        entity_type: str = None,
        resource_share_id: str = None,
        association_status_message: str = None,
        association_type: str = None,
        association_status: str = None,
    ):
        self.update_time = update_time
        self.entity_id = entity_id
        self.resource_share_name = resource_share_name
        self.create_time = create_time
        self.entity_type = entity_type
        self.resource_share_id = resource_share_id
        self.association_status_message = association_status_message
        self.association_type = association_type
        self.association_status = association_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        return self


class ListResourceShareAssociationsResponseBody(TeaModel):
    def __init__(
        self,
        resource_share_associations: List[ListResourceShareAssociationsResponseBodyResourceShareAssociations] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.resource_share_associations = resource_share_associations
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.resource_share_associations:
            for k in self.resource_share_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k in m.get('ResourceShareAssociations'):
                temp_model = ListResourceShareAssociationsResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourceShareAssociationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResourceShareAssociationsResponseBody = None,
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
            temp_model = ListResourceShareAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceSharesRequest(TeaModel):
    def __init__(
        self,
        resource_owner: str = None,
        resource_share_name: str = None,
        resource_share_status: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_share_ids: List[str] = None,
    ):
        self.resource_owner = resource_owner
        self.resource_share_name = resource_share_name
        self.resource_share_status = resource_share_status
        self.max_results = max_results
        self.next_token = next_token
        self.resource_share_ids = resource_share_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        return self


class ListResourceSharesResponseBodyResourceShares(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        resource_share_name: str = None,
        resource_share_owner: str = None,
        create_time: str = None,
        resource_share_id: str = None,
        resource_share_status: str = None,
    ):
        self.update_time = update_time
        self.resource_share_name = resource_share_name
        self.resource_share_owner = resource_share_owner
        self.create_time = create_time
        self.resource_share_id = resource_share_id
        self.resource_share_status = resource_share_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        return self


class ListResourceSharesResponseBody(TeaModel):
    def __init__(
        self,
        resource_shares: List[ListResourceSharesResponseBodyResourceShares] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.resource_shares = resource_shares
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.resource_shares:
            for k in self.resource_shares:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResourceShares'] = []
        if self.resource_shares is not None:
            for k in self.resource_shares:
                result['ResourceShares'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_shares = []
        if m.get('ResourceShares') is not None:
            for k in m.get('ResourceShares'):
                temp_model = ListResourceSharesResponseBodyResourceShares()
                self.resource_shares.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourceSharesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListResourceSharesResponseBody = None,
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
            temp_model = ListResourceSharesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSharedResourcesRequest(TeaModel):
    def __init__(
        self,
        resource_owner: str = None,
        resource_type: str = None,
        target: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_share_ids: List[str] = None,
        resource_ids: List[str] = None,
    ):
        self.resource_owner = resource_owner
        self.resource_type = resource_type
        self.target = target
        self.max_results = max_results
        self.next_token = next_token
        self.resource_share_ids = resource_share_ids
        self.resource_ids = resource_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.target is not None:
            result['Target'] = self.target
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        return self


class ListSharedResourcesResponseBodySharedResources(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        resource_type: str = None,
        create_time: str = None,
        resource_share_id: str = None,
        resource_id: str = None,
        resource_status: str = None,
        resource_status_message: str = None,
    ):
        self.update_time = update_time
        self.resource_type = resource_type
        self.create_time = create_time
        self.resource_share_id = resource_share_id
        self.resource_id = resource_id
        self.resource_status = resource_status
        self.resource_status_message = resource_status_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_status_message is not None:
            result['ResourceStatusMessage'] = self.resource_status_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceStatusMessage') is not None:
            self.resource_status_message = m.get('ResourceStatusMessage')
        return self


class ListSharedResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        shared_resources: List[ListSharedResourcesResponseBodySharedResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.shared_resources = shared_resources

    def validate(self):
        if self.shared_resources:
            for k in self.shared_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SharedResources'] = []
        if self.shared_resources is not None:
            for k in self.shared_resources:
                result['SharedResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.shared_resources = []
        if m.get('SharedResources') is not None:
            for k in m.get('SharedResources'):
                temp_model = ListSharedResourcesResponseBodySharedResources()
                self.shared_resources.append(temp_model.from_map(k))
        return self


class ListSharedResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSharedResourcesResponseBody = None,
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
            temp_model = ListSharedResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSharedTargetsRequest(TeaModel):
    def __init__(
        self,
        resource_owner: str = None,
        resource_type: str = None,
        resource_id: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_share_ids: List[str] = None,
        targets: List[str] = None,
    ):
        self.resource_owner = resource_owner
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.max_results = max_results
        self.next_token = next_token
        self.resource_share_ids = resource_share_ids
        self.targets = targets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class ListSharedTargetsResponseBodySharedTargets(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        create_time: str = None,
        resource_share_id: str = None,
        target_id: str = None,
    ):
        self.update_time = update_time
        self.create_time = create_time
        self.resource_share_id = resource_share_id
        self.target_id = target_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        return self


class ListSharedTargetsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        shared_targets: List[ListSharedTargetsResponseBodySharedTargets] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.shared_targets = shared_targets

    def validate(self):
        if self.shared_targets:
            for k in self.shared_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SharedTargets'] = []
        if self.shared_targets is not None:
            for k in self.shared_targets:
                result['SharedTargets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.shared_targets = []
        if m.get('SharedTargets') is not None:
            for k in m.get('SharedTargets'):
                temp_model = ListSharedTargetsResponseBodySharedTargets()
                self.shared_targets.append(temp_model.from_map(k))
        return self


class ListSharedTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSharedTargetsResponseBody = None,
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
            temp_model = ListSharedTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceShareRequest(TeaModel):
    def __init__(
        self,
        resource_share_id: str = None,
        resource_share_name: str = None,
    ):
        self.resource_share_id = resource_share_id
        self.resource_share_name = resource_share_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        return self


class UpdateResourceShareResponseBodyResourceShare(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        resource_share_name: str = None,
        resource_share_owner: str = None,
        create_time: str = None,
        resource_share_id: str = None,
        resource_share_status: str = None,
    ):
        self.update_time = update_time
        self.resource_share_name = resource_share_name
        self.resource_share_owner = resource_share_owner
        self.create_time = create_time
        self.resource_share_id = resource_share_id
        self.resource_share_status = resource_share_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        return self


class UpdateResourceShareResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_share: UpdateResourceShareResponseBodyResourceShare = None,
    ):
        self.request_id = request_id
        self.resource_share = resource_share

    def validate(self):
        if self.resource_share:
            self.resource_share.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_share is not None:
            result['ResourceShare'] = self.resource_share.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceShare') is not None:
            temp_model = UpdateResourceShareResponseBodyResourceShare()
            self.resource_share = temp_model.from_map(m['ResourceShare'])
        return self


class UpdateResourceShareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateResourceShareResponseBody = None,
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
            temp_model = UpdateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


