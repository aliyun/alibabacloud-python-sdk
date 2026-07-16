# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class AddRegisterLineageRequest(DaraModel):
    def __init__(
        self,
        add_register_lineage_command: main_models.AddRegisterLineageRequestAddRegisterLineageCommand = None,
        op_tenant_id: int = None,
    ):
        # The command for registering and adding data lineage.
        # 
        # This parameter is required.
        self.add_register_lineage_command = add_register_lineage_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.add_register_lineage_command:
            self.add_register_lineage_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_register_lineage_command is not None:
            result['AddRegisterLineageCommand'] = self.add_register_lineage_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddRegisterLineageCommand') is not None:
            temp_model = main_models.AddRegisterLineageRequestAddRegisterLineageCommand()
            self.add_register_lineage_command = temp_model.from_map(m.get('AddRegisterLineageCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class AddRegisterLineageRequestAddRegisterLineageCommand(DaraModel):
    def __init__(
        self,
        check_asset_exist: bool = None,
        detailed_lineages: List[main_models.AddRegisterLineageRequestAddRegisterLineageCommandDetailedLineages] = None,
        relation_properties: Dict[str, Any] = None,
        source: main_models.AddRegisterLineageRequestAddRegisterLineageCommandSource = None,
        target: main_models.AddRegisterLineageRequestAddRegisterLineageCommandTarget = None,
        tenant_id: int = None,
        user_id: str = None,
    ):
        # Specifies whether to check the existence of the asset. By default, the existence is not checked.
        self.check_asset_exist = check_asset_exist
        # The detailed lineage relationships. For tables, these are field-level lineage relationships. If you do not want to add field-level lineage, leave this parameter empty.
        self.detailed_lineages = detailed_lineages
        # The lineage relationship properties.
        self.relation_properties = relation_properties
        # The source asset.
        # 
        # This parameter is required.
        self.source = source
        # The target asset.
        # 
        # This parameter is required.
        self.target = target
        # The tenant ID.
        self.tenant_id = tenant_id
        # The ID of the current user.
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
        if self.check_asset_exist is not None:
            result['CheckAssetExist'] = self.check_asset_exist

        result['DetailedLineages'] = []
        if self.detailed_lineages is not None:
            for k1 in self.detailed_lineages:
                result['DetailedLineages'].append(k1.to_map() if k1 else None)

        if self.relation_properties is not None:
            result['RelationProperties'] = self.relation_properties

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
        if m.get('CheckAssetExist') is not None:
            self.check_asset_exist = m.get('CheckAssetExist')

        self.detailed_lineages = []
        if m.get('DetailedLineages') is not None:
            for k1 in m.get('DetailedLineages'):
                temp_model = main_models.AddRegisterLineageRequestAddRegisterLineageCommandDetailedLineages()
                self.detailed_lineages.append(temp_model.from_map(k1))

        if m.get('RelationProperties') is not None:
            self.relation_properties = m.get('RelationProperties')

        if m.get('Source') is not None:
            temp_model = main_models.AddRegisterLineageRequestAddRegisterLineageCommandSource()
            self.source = temp_model.from_map(m.get('Source'))

        if m.get('Target') is not None:
            temp_model = main_models.AddRegisterLineageRequestAddRegisterLineageCommandTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class AddRegisterLineageRequestAddRegisterLineageCommandTarget(DaraModel):
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
        # The catalog property of the asset. For tables, the catalog of both compute source tables and logical tables is uniformly set to dataphin. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.catalog = catalog
        # The environment to which the asset belongs. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.env = env
        # The extended properties.
        self.ext_properties = ext_properties
        # The GUID of the asset. This parameter is required when referenceType is set to BY_GUID.
        self.guid = guid
        # The asset subtype. Specify this parameter only when metadataType is set to TABLE and referenceType is not set to BY_GUID.
        self.metadata_sub_type = metadata_sub_type
        # The asset type. Set this parameter based on the actual scenario.
        # 
        # This parameter is required.
        self.metadata_type = metadata_type
        # The name of the asset. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.name = name
        # The asset reference data type. Valid values: BY_GUID and BY_PROPERTY.
        # 
        # This parameter is required.
        self.reference_type = reference_type
        # The schema property of the asset. For tables, this is typically the project or business unit. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
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

class AddRegisterLineageRequestAddRegisterLineageCommandSource(DaraModel):
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
        # The catalog property of the asset. For tables, the catalog of both compute source tables and logical tables is uniformly set to dataphin. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.catalog = catalog
        # The environment to which the asset belongs. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.env = env
        # The extended properties.
        self.ext_properties = ext_properties
        # The GUID of the asset. This parameter is required when referenceType is set to BY_GUID.
        self.guid = guid
        # The asset subtype. Specify this parameter only when metadataType is set to TABLE and referenceType is not set to BY_GUID.
        self.metadata_sub_type = metadata_sub_type
        # The asset type. Set this parameter based on the actual scenario.
        # 
        # This parameter is required.
        self.metadata_type = metadata_type
        # The name of the asset. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.name = name
        # The asset reference data type. Valid values: BY_GUID and BY_PROPERTY.
        # 
        # This parameter is required.
        self.reference_type = reference_type
        # The schema property of the asset. For tables, this is typically the project or business unit. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
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

class AddRegisterLineageRequestAddRegisterLineageCommandDetailedLineages(DaraModel):
    def __init__(
        self,
        is_direct: bool = None,
        source: main_models.AddRegisterLineageRequestAddRegisterLineageCommandDetailedLineagesSource = None,
        target: main_models.AddRegisterLineageRequestAddRegisterLineageCommandDetailedLineagesTarget = None,
    ):
        # Specifies whether this is a direct lineage relationship. Default value: true.
        self.is_direct = is_direct
        # The source asset reference.
        # 
        # This parameter is required.
        self.source = source
        # The target asset reference.
        # 
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
            temp_model = main_models.AddRegisterLineageRequestAddRegisterLineageCommandDetailedLineagesSource()
            self.source = temp_model.from_map(m.get('Source'))

        if m.get('Target') is not None:
            temp_model = main_models.AddRegisterLineageRequestAddRegisterLineageCommandDetailedLineagesTarget()
            self.target = temp_model.from_map(m.get('Target'))

        return self

class AddRegisterLineageRequestAddRegisterLineageCommandDetailedLineagesTarget(DaraModel):
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
        # The catalog property of the asset. For tables, the catalog of both compute source tables and logical tables is uniformly set to dataphin. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.catalog = catalog
        # The environment to which the asset belongs. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.env = env
        # The extended properties.
        self.ext_properties = ext_properties
        # The GUID of the asset. This parameter is required when referenceType is set to BY_GUID.
        self.guid = guid
        # The asset type. Set this parameter based on the actual scenario.
        self.metadata_type = metadata_type
        # The name of the asset. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.name = name
        # The GUID of the parent asset. If the current object is a field, parentGuid is the GUID of the table to which the field belongs.
        self.parent_guid = parent_guid
        # The asset reference data type. Valid values: BY_GUID and BY_PROPERTY.
        self.reference_type = reference_type
        # The schema property of the asset. For tables, this is typically the project or business unit. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
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

class AddRegisterLineageRequestAddRegisterLineageCommandDetailedLineagesSource(DaraModel):
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
        # The catalog property of the asset. For tables, the catalog of both compute source tables and logical tables is uniformly set to dataphin. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.catalog = catalog
        # The environment to which the asset belongs. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.env = env
        # The extended properties.
        self.ext_properties = ext_properties
        # The GUID of the asset. This parameter is required when referenceType is set to BY_GUID.
        self.guid = guid
        # The asset type. Set this parameter based on the actual scenario.
        self.metadata_type = metadata_type
        # The name of the asset. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
        self.name = name
        # The GUID of the parent asset. If the current object is a field, parentGuid is the GUID of the table to which the field belongs.
        self.parent_guid = parent_guid
        # The asset reference data type. Valid values: BY_GUID and BY_PROPERTY.
        self.reference_type = reference_type
        # The schema property of the asset. For tables, this is typically the project or business unit. This property is used to identify the corresponding asset by property when referenceType is set to BY_PROPERTY. If referenceType is set to BY_GUID, this property does not need to be specified.
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

