# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class DeleteRegisterLineageRequest(DaraModel):
    def __init__(
        self,
        delete_register_lineage_command: main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.delete_register_lineage_command = delete_register_lineage_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.delete_register_lineage_command:
            self.delete_register_lineage_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_register_lineage_command is not None:
            result['DeleteRegisterLineageCommand'] = self.delete_register_lineage_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteRegisterLineageCommand') is not None:
            temp_model = main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommand()
            self.delete_register_lineage_command = temp_model.from_map(m.get('DeleteRegisterLineageCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class DeleteRegisterLineageRequestDeleteRegisterLineageCommand(DaraModel):
    def __init__(
        self,
        cascade_delete_lineage: bool = None,
        detailed_lineages: List[main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandDetailedLineages] = None,
        source: main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandSource = None,
        target: main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandTarget = None,
        tenant_id: int = None,
        user_id: str = None,
    ):
        self.cascade_delete_lineage = cascade_delete_lineage
        self.detailed_lineages = detailed_lineages
        # This parameter is required.
        self.source = source
        # This parameter is required.
        self.target = target
        self.tenant_id = tenant_id
        self.user_id = user_id

    def validate(self):
        if self.detailed_lineages:
            for v1 in self.detailed_lineages:
                 if v1:
                    v1.validate()
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cascade_delete_lineage is not None:
            result['CascadeDeleteLineage'] = self.cascade_delete_lineage

        result['DetailedLineages'] = []
        if self.detailed_lineages is not None:
            for k1 in self.detailed_lineages:
                result['DetailedLineages'].append(k1.to_map() if k1 else None)

        if self.source is not None:
            result['Source'] = self.source.to_map()

        if self.target is not None:
            result['Target'] = self.target.to_map()

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CascadeDeleteLineage') is not None:
            self.cascade_delete_lineage = m.get('CascadeDeleteLineage')

        self.detailed_lineages = []
        if m.get('DetailedLineages') is not None:
            for k1 in m.get('DetailedLineages'):
                temp_model = main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandDetailedLineages()
                self.detailed_lineages.append(temp_model.from_map(k1))

        if m.get('Source') is not None:
            temp_model = main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandSource()
            self.source = temp_model.from_map(m.get('Source'))

        if m.get('Target') is not None:
            temp_model = main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DeleteRegisterLineageRequestDeleteRegisterLineageCommandTarget(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        env: str = None,
        ext_properties: Dict[str, Any] = None,
        guid: str = None,
        metadata_sub_type: str = None,
        metadata_type: str = None,
        name: str = None,
        reference_type: str = None,
        schema: str = None,
    ):
        self.catalog = catalog
        self.env = env
        self.ext_properties = ext_properties
        self.guid = guid
        self.metadata_sub_type = metadata_sub_type
        # This parameter is required.
        self.metadata_type = metadata_type
        self.name = name
        # This parameter is required.
        self.reference_type = reference_type
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.env is not None:
            result['Env'] = self.env

        if self.ext_properties is not None:
            result['ExtProperties'] = self.ext_properties

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.metadata_sub_type is not None:
            result['MetadataSubType'] = self.metadata_sub_type

        if self.metadata_type is not None:
            result['MetadataType'] = self.metadata_type

        if self.name is not None:
            result['Name'] = self.name

        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ExtProperties') is not None:
            self.ext_properties = m.get('ExtProperties')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('MetadataSubType') is not None:
            self.metadata_sub_type = m.get('MetadataSubType')

        if m.get('MetadataType') is not None:
            self.metadata_type = m.get('MetadataType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self

class DeleteRegisterLineageRequestDeleteRegisterLineageCommandSource(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        env: str = None,
        ext_properties: Dict[str, Any] = None,
        guid: str = None,
        metadata_sub_type: str = None,
        metadata_type: str = None,
        name: str = None,
        reference_type: str = None,
        schema: str = None,
    ):
        self.catalog = catalog
        self.env = env
        self.ext_properties = ext_properties
        self.guid = guid
        self.metadata_sub_type = metadata_sub_type
        # This parameter is required.
        self.metadata_type = metadata_type
        self.name = name
        # This parameter is required.
        self.reference_type = reference_type
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.env is not None:
            result['Env'] = self.env

        if self.ext_properties is not None:
            result['ExtProperties'] = self.ext_properties

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.metadata_sub_type is not None:
            result['MetadataSubType'] = self.metadata_sub_type

        if self.metadata_type is not None:
            result['MetadataType'] = self.metadata_type

        if self.name is not None:
            result['Name'] = self.name

        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ExtProperties') is not None:
            self.ext_properties = m.get('ExtProperties')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('MetadataSubType') is not None:
            self.metadata_sub_type = m.get('MetadataSubType')

        if m.get('MetadataType') is not None:
            self.metadata_type = m.get('MetadataType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self

class DeleteRegisterLineageRequestDeleteRegisterLineageCommandDetailedLineages(DaraModel):
    def __init__(
        self,
        is_direct: bool = None,
        source: main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandDetailedLineagesSource = None,
        target: main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandDetailedLineagesTarget = None,
    ):
        self.is_direct = is_direct
        # This parameter is required.
        self.source = source
        # This parameter is required.
        self.target = target

    def validate(self):
        if self.source:
            self.source.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_direct is not None:
            result['IsDirect'] = self.is_direct

        if self.source is not None:
            result['Source'] = self.source.to_map()

        if self.target is not None:
            result['Target'] = self.target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDirect') is not None:
            self.is_direct = m.get('IsDirect')

        if m.get('Source') is not None:
            temp_model = main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandDetailedLineagesSource()
            self.source = temp_model.from_map(m.get('Source'))

        if m.get('Target') is not None:
            temp_model = main_models.DeleteRegisterLineageRequestDeleteRegisterLineageCommandDetailedLineagesTarget()
            self.target = temp_model.from_map(m.get('Target'))

        return self

class DeleteRegisterLineageRequestDeleteRegisterLineageCommandDetailedLineagesTarget(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        env: str = None,
        ext_properties: Dict[str, Any] = None,
        guid: str = None,
        metadata_type: str = None,
        name: str = None,
        parent_guid: str = None,
        reference_type: str = None,
        schema: str = None,
    ):
        self.catalog = catalog
        self.env = env
        self.ext_properties = ext_properties
        self.guid = guid
        self.metadata_type = metadata_type
        self.name = name
        self.parent_guid = parent_guid
        self.reference_type = reference_type
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.env is not None:
            result['Env'] = self.env

        if self.ext_properties is not None:
            result['ExtProperties'] = self.ext_properties

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.metadata_type is not None:
            result['MetadataType'] = self.metadata_type

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_guid is not None:
            result['ParentGuid'] = self.parent_guid

        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ExtProperties') is not None:
            self.ext_properties = m.get('ExtProperties')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('MetadataType') is not None:
            self.metadata_type = m.get('MetadataType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentGuid') is not None:
            self.parent_guid = m.get('ParentGuid')

        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self

class DeleteRegisterLineageRequestDeleteRegisterLineageCommandDetailedLineagesSource(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        env: str = None,
        ext_properties: Dict[str, Any] = None,
        guid: str = None,
        metadata_type: str = None,
        name: str = None,
        parent_guid: str = None,
        reference_type: str = None,
        schema: str = None,
    ):
        self.catalog = catalog
        self.env = env
        self.ext_properties = ext_properties
        self.guid = guid
        self.metadata_type = metadata_type
        self.name = name
        self.parent_guid = parent_guid
        self.reference_type = reference_type
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.env is not None:
            result['Env'] = self.env

        if self.ext_properties is not None:
            result['ExtProperties'] = self.ext_properties

        if self.guid is not None:
            result['Guid'] = self.guid

        if self.metadata_type is not None:
            result['MetadataType'] = self.metadata_type

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_guid is not None:
            result['ParentGuid'] = self.parent_guid

        if self.reference_type is not None:
            result['ReferenceType'] = self.reference_type

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ExtProperties') is not None:
            self.ext_properties = m.get('ExtProperties')

        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('MetadataType') is not None:
            self.metadata_type = m.get('MetadataType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentGuid') is not None:
            self.parent_guid = m.get('ParentGuid')

        if m.get('ReferenceType') is not None:
            self.reference_type = m.get('ReferenceType')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self

