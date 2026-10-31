# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListStandardsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListStandardsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # The paged query result.
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListStandardsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        standard_list: List[main_models.ListStandardsResponseBodyPageResultStandardList] = None,
        total_count: int = None,
    ):
        # The standard list.
        self.standard_list = standard_list
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.standard_list:
            for v1 in self.standard_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StandardList'] = []
        if self.standard_list is not None:
            for k1 in self.standard_list:
                result['StandardList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.standard_list = []
        if m.get('StandardList') is not None:
            for k1 in m.get('StandardList'):
                temp_model = main_models.ListStandardsResponseBodyPageResultStandardList()
                self.standard_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListStandardsResponseBodyPageResultStandardList(DaraModel):
    def __init__(
        self,
        attribute_with_value_list: List[main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueList] = None,
        code: str = None,
        creator: main_models.ListStandardsResponseBodyPageResultStandardListCreator = None,
        description: str = None,
        effective_time_config: main_models.ListStandardsResponseBodyPageResultStandardListEffectiveTimeConfig = None,
        english_name: str = None,
        id: int = None,
        last_modifier: main_models.ListStandardsResponseBodyPageResultStandardListLastModifier = None,
        modify_time: str = None,
        name: str = None,
        owner: main_models.ListStandardsResponseBodyPageResultStandardListOwner = None,
        stage: str = None,
        standard_set: main_models.ListStandardsResponseBodyPageResultStandardListStandardSet = None,
        standard_template: main_models.ListStandardsResponseBodyPageResultStandardListStandardTemplate = None,
        status: str = None,
        type: str = None,
        version: int = None,
    ):
        # The attribute value configuration.
        self.attribute_with_value_list = attribute_with_value_list
        # The code of the standard.
        self.code = code
        # The creator.
        self.creator = creator
        # The description.
        self.description = description
        # The effective period configuration.
        self.effective_time_config = effective_time_config
        # The English name of the standard.
        self.english_name = english_name
        # The standard ID.
        self.id = id
        # The user who last updated the standard.
        self.last_modifier = last_modifier
        # The last modified time. The format is YYYY-MM-DD HH:mm:ss.
        self.modify_time = modify_time
        # The name of the standard.
        self.name = name
        # The owner.
        self.owner = owner
        # The stage of the standard.
        self.stage = stage
        # The standard set that the current standard depends on.
        self.standard_set = standard_set
        # The standard template that the current standard depends on.
        self.standard_template = standard_template
        # The status of the standard.
        self.status = status
        # The type of the standard.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.attribute_with_value_list:
            for v1 in self.attribute_with_value_list:
                 if v1:
                    v1.validate()
        if self.creator:
            self.creator.validate()
        if self.effective_time_config:
            self.effective_time_config.validate()
        if self.last_modifier:
            self.last_modifier.validate()
        if self.owner:
            self.owner.validate()
        if self.standard_set:
            self.standard_set.validate()
        if self.standard_template:
            self.standard_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeWithValueList'] = []
        if self.attribute_with_value_list is not None:
            for k1 in self.attribute_with_value_list:
                result['AttributeWithValueList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.effective_time_config is not None:
            result['EffectiveTimeConfig'] = self.effective_time_config.to_map()

        if self.english_name is not None:
            result['EnglishName'] = self.english_name

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier.to_map()

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner.to_map()

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.standard_set is not None:
            result['StandardSet'] = self.standard_set.to_map()

        if self.standard_template is not None:
            result['StandardTemplate'] = self.standard_template.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_with_value_list = []
        if m.get('AttributeWithValueList') is not None:
            for k1 in m.get('AttributeWithValueList'):
                temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueList()
                self.attribute_with_value_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Creator') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectiveTimeConfig') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListEffectiveTimeConfig()
            self.effective_time_config = temp_model.from_map(m.get('EffectiveTimeConfig'))

        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListLastModifier()
            self.last_modifier = temp_model.from_map(m.get('LastModifier'))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListOwner()
            self.owner = temp_model.from_map(m.get('Owner'))

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('StandardSet') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListStandardSet()
            self.standard_set = temp_model.from_map(m.get('StandardSet'))

        if m.get('StandardTemplate') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListStandardTemplate()
            self.standard_template = temp_model.from_map(m.get('StandardTemplate'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListStandardsResponseBodyPageResultStandardListStandardTemplate(DaraModel):
    def __init__(
        self,
        code: str = None,
        id: int = None,
        name: str = None,
        template_from: str = None,
        version: int = None,
    ):
        # The code of the standard template.
        self.code = code
        # The ID of the standard template.
        self.id = id
        # The name of the standard template.
        self.name = name
        # The source of the standard template. Valid values:
        # - CUSTOM: Custom standard template.
        # - SYSTEM: Built-in standard template.
        self.template_from = template_from
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.template_from is not None:
            result['TemplateFrom'] = self.template_from

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateFrom') is not None:
            self.template_from = m.get('TemplateFrom')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListStandardsResponseBodyPageResultStandardListStandardSet(DaraModel):
    def __init__(
        self,
        code: str = None,
        directory: str = None,
        id: int = None,
        name: str = None,
    ):
        # The code of the standard set.
        self.code = code
        # The folder to which the standard set belongs.
        self.directory = directory
        # The ID of the standard set.
        self.id = id
        # The name of the standard set.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListStandardsResponseBodyPageResultStandardListOwner(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the user.
        self.id = id
        # The name of the user.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListStandardsResponseBodyPageResultStandardListLastModifier(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the user.
        self.id = id
        # The name of the user.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListStandardsResponseBodyPageResultStandardListEffectiveTimeConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The end time of the effective period. The format is YYYY-MM-DD HH:mm:ss.
        self.end_time = end_time
        # The start time of the effective period. The format is YYYY-MM-DD HH:mm:ss.
        self.start_time = start_time
        # The effective period type. Valid values:
        # - FOREVER: Permanent.
        # - TIME_PERIOD: Time period.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListStandardsResponseBodyPageResultStandardListCreator(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The ID of the user.
        self.id = id
        # The name of the user.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueList(DaraModel):
    def __init__(
        self,
        attribute: main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttribute = None,
        value: str = None,
    ):
        # The attribute details.
        self.attribute = attribute
        # The attribute value.
        self.value = value

    def validate(self):
        if self.attribute:
            self.attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute.to_map()

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttribute()
            self.attribute = temp_model.from_map(m.get('Attribute'))

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttribute(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        enable_monitor_config: bool = None,
        id: int = None,
        monitor_config: main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeMonitorConfig = None,
        name: str = None,
        ref_attribute: main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeRefAttribute = None,
        required: bool = None,
        type: str = None,
        value_config: main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfig = None,
    ):
        # The attribute code.
        self.code = code
        # The description.
        self.description = description
        # Specifies whether to enable the monitoring configuration.
        self.enable_monitor_config = enable_monitor_config
        # The ID of the attribute.
        self.id = id
        # The monitoring configuration.
        self.monitor_config = monitor_config
        # The attribute name.
        self.name = name
        # The referenced attribute information.
        self.ref_attribute = ref_attribute
        # Specifies whether the attribute is required.
        self.required = required
        # The attribute type. Valid values: BIZ_ATTRIBUTE: business attribute. TECH_ATTRIBUTE: technical attribute. MANAGEMENT_ATTRIBUTE: management attribute. QUALITY_ATTRIBUTE: quality attribute. MASTER_DATA_ATTRIBUTE: master data attribute. LIFECYCLE_ATTRIBUTE: lifecycle attribute. SECURITY_ATTRIBUTE: security attribute.
        self.type = type
        # The value configuration.
        self.value_config = value_config

    def validate(self):
        if self.monitor_config:
            self.monitor_config.validate()
        if self.ref_attribute:
            self.ref_attribute.validate()
        if self.value_config:
            self.value_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_monitor_config is not None:
            result['EnableMonitorConfig'] = self.enable_monitor_config

        if self.id is not None:
            result['Id'] = self.id

        if self.monitor_config is not None:
            result['MonitorConfig'] = self.monitor_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.ref_attribute is not None:
            result['RefAttribute'] = self.ref_attribute.to_map()

        if self.required is not None:
            result['Required'] = self.required

        if self.type is not None:
            result['Type'] = self.type

        if self.value_config is not None:
            result['ValueConfig'] = self.value_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableMonitorConfig') is not None:
            self.enable_monitor_config = m.get('EnableMonitorConfig')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MonitorConfig') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeMonitorConfig()
            self.monitor_config = temp_model.from_map(m.get('MonitorConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RefAttribute') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeRefAttribute()
            self.ref_attribute = temp_model.from_map(m.get('RefAttribute'))

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueConfig') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfig()
            self.value_config = temp_model.from_map(m.get('ValueConfig'))

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfig(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        default_value: str = None,
        length: int = None,
        type: str = None,
        value_range: main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfigValueRange = None,
    ):
        # The data type of the attribute value. Valid values: STRING: string. BIGINT: numeric type. DOUBLE: floating-point type. DATE: date accurate to day. DATETIME: date accurate to millisecond. BOOLEAN: Boolean type.
        self.data_type = data_type
        # The default value.
        self.default_value = default_value
        # The length of the attribute value. An empty value or -1 indicates that the length is not limited. Typically, only the string type limits the length of the attribute value.
        self.length = length
        # The attribute value type. Valid values: CUSTOMIZED: custom input. SINGLE_ENUM: single enum value. MULTIPLE_ENUMS: multiple enum values. RANGE: range value.
        self.type = type
        # The value range.
        self.value_range = value_range

    def validate(self):
        if self.value_range:
            self.value_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.length is not None:
            result['Length'] = self.length

        if self.type is not None:
            result['Type'] = self.type

        if self.value_range is not None:
            result['ValueRange'] = self.value_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueRange') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfigValueRange()
            self.value_range = temp_model.from_map(m.get('ValueRange'))

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfigValueRange(DaraModel):
    def __init__(
        self,
        dataphin_attribute_type: str = None,
        lookup_table_reference: main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfigValueRangeLookupTableReference = None,
        min_max_value_config: main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfigValueRangeMinMaxValueConfig = None,
        value_constraint: str = None,
        value_list: List[str] = None,
    ):
        # The value range. This parameter takes effect when the value source is set to DATAPHIN_ATTRIBUTE. Valid values: BIZ_UNIT: data block. PROJECT: project. USER: user. USER_GROUP: user group.
        self.dataphin_attribute_type = dataphin_attribute_type
        # The value range. This parameter takes effect when the value source is set to LOOKUP_TABLE.
        self.lookup_table_reference = lookup_table_reference
        # The value range. This parameter takes effect when the value source is set to MIN_MAX.
        self.min_max_value_config = min_max_value_config
        # The value source. Valid values: NONE: no constraint. LIST: obtained from a list. LOOKUP_TABLE: lookup table. MIN_MAX: obtained between the maximum and minimum values. DATAPHIN_ATTRIBUTE: Dataphin system property. BUILT_IN_DATA_TYPES: built-in data type. BUILT_IN_DATA_CLASSIFICATION: built-in data categorization. BUILT_IN_DATA_LEVEL: built-in data security classification.
        self.value_constraint = value_constraint
        # The value range. This parameter takes effect when the value source is set to LIST.
        self.value_list = value_list

    def validate(self):
        if self.lookup_table_reference:
            self.lookup_table_reference.validate()
        if self.min_max_value_config:
            self.min_max_value_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataphin_attribute_type is not None:
            result['DataphinAttributeType'] = self.dataphin_attribute_type

        if self.lookup_table_reference is not None:
            result['LookupTableReference'] = self.lookup_table_reference.to_map()

        if self.min_max_value_config is not None:
            result['MinMaxValueConfig'] = self.min_max_value_config.to_map()

        if self.value_constraint is not None:
            result['ValueConstraint'] = self.value_constraint

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataphinAttributeType') is not None:
            self.dataphin_attribute_type = m.get('DataphinAttributeType')

        if m.get('LookupTableReference') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfigValueRangeLookupTableReference()
            self.lookup_table_reference = temp_model.from_map(m.get('LookupTableReference'))

        if m.get('MinMaxValueConfig') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfigValueRangeMinMaxValueConfig()
            self.min_max_value_config = temp_model.from_map(m.get('MinMaxValueConfig'))

        if m.get('ValueConstraint') is not None:
            self.value_constraint = m.get('ValueConstraint')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfigValueRangeMinMaxValueConfig(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
    ):
        # Specifies whether to include the maximum value.
        self.include_max_value = include_max_value
        # Specifies whether to include the minimum value.
        self.include_min_value = include_min_value
        # The maximum value.
        self.max_value = max_value
        # The minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_max_value is not None:
            result['IncludeMaxValue'] = self.include_max_value

        if self.include_min_value is not None:
            result['IncludeMinValue'] = self.include_min_value

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeMaxValue') is not None:
            self.include_max_value = m.get('IncludeMaxValue')

        if m.get('IncludeMinValue') is not None:
            self.include_min_value = m.get('IncludeMinValue')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeValueConfigValueRangeLookupTableReference(DaraModel):
    def __init__(
        self,
        column: str = None,
        lookup_table_id: int = None,
    ):
        # The referenced field in the lookup table.
        self.column = column
        # The ID of the lookup table.
        self.lookup_table_id = lookup_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.lookup_table_id is not None:
            result['LookupTableId'] = self.lookup_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('LookupTableId') is not None:
            self.lookup_table_id = m.get('LookupTableId')

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeRefAttribute(DaraModel):
    def __init__(
        self,
        attribute_from_info: main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeRefAttributeAttributeFromInfo = None,
        attribute_id: int = None,
    ):
        # The source of the attribute.
        self.attribute_from_info = attribute_from_info
        # The ID of the attribute.
        self.attribute_id = attribute_id

    def validate(self):
        if self.attribute_from_info:
            self.attribute_from_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_from_info is not None:
            result['AttributeFromInfo'] = self.attribute_from_info.to_map()

        if self.attribute_id is not None:
            result['AttributeId'] = self.attribute_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeFromInfo') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeRefAttributeAttributeFromInfo()
            self.attribute_from_info = temp_model.from_map(m.get('AttributeFromInfo'))

        if m.get('AttributeId') is not None:
            self.attribute_id = m.get('AttributeId')

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeRefAttributeAttributeFromInfo(DaraModel):
    def __init__(
        self,
        attribute_from: str = None,
        standard_reference: main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeRefAttributeAttributeFromInfoStandardReference = None,
    ):
        # The source of the attribute. Valid values: SYSTEM: system attribute. CUSTOM: custom attribute. STANDARD: standard.
        self.attribute_from = attribute_from
        # The corresponding standard. This parameter takes effect when the attribute source is set to STANDARD.
        self.standard_reference = standard_reference

    def validate(self):
        if self.standard_reference:
            self.standard_reference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_from is not None:
            result['AttributeFrom'] = self.attribute_from

        if self.standard_reference is not None:
            result['StandardReference'] = self.standard_reference.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeFrom') is not None:
            self.attribute_from = m.get('AttributeFrom')

        if m.get('StandardReference') is not None:
            temp_model = main_models.ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeRefAttributeAttributeFromInfoStandardReference()
            self.standard_reference = temp_model.from_map(m.get('StandardReference'))

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeRefAttributeAttributeFromInfoStandardReference(DaraModel):
    def __init__(
        self,
        standard_id: int = None,
        version: int = None,
    ):
        # The ID of the standard.
        self.standard_id = standard_id
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListStandardsResponseBodyPageResultStandardListAttributeWithValueListAttributeMonitorConfig(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        is_case_sensitive: bool = None,
        type: str = None,
    ):
        # The field to be checked.
        self.column_name = column_name
        # Specifies whether the check is case-sensitive.
        self.is_case_sensitive = is_case_sensitive
        # The monitoring method. Valid values: METADATA: metadata monitoring. QUALITY: data quality monitoring.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.is_case_sensitive is not None:
            result['IsCaseSensitive'] = self.is_case_sensitive

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('IsCaseSensitive') is not None:
            self.is_case_sensitive = m.get('IsCaseSensitive')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

