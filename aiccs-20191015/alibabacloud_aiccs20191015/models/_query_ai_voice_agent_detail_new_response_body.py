# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryAiVoiceAgentDetailNewResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QueryAiVoiceAgentDetailNewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The reason for the access denial.
        self.access_denied_detail = access_denied_detail
        # Status code.
        self.code = code
        # The detailed data of the agent.
        self.data = data
        # The message that is associated with the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the API call was successful. Possible values:
        # 
        # - **true**: The operation was successful.
        # 
        # - **false**: Failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_call_config: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfig = None,
        agent_demand_config: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentDemandConfig = None,
        agent_desc: str = None,
        agent_id: int = None,
        agent_mode: int = None,
        agent_name: str = None,
        branch_deploy_status: int = None,
        branch_desc: str = None,
        branch_id: int = None,
        branch_name: str = None,
        knowledge_config: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataKnowledgeConfig = None,
        phone_tag_config: List[main_models.QueryAiVoiceAgentDetailNewResponseBodyDataPhoneTagConfig] = None,
        scene: str = None,
        summary_config: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfig = None,
        version_desc: str = None,
        version_id: int = None,
        version_name: str = None,
        version_publish_status: int = None,
        version_publish_time: str = None,
    ):
        # The voice configuration for intelligent outbound calls.
        self.agent_call_config = agent_call_config
        # The business requirement configuration for the agent.
        self.agent_demand_config = agent_demand_config
        # The agent description.
        self.agent_desc = agent_desc
        # The agent ID.
        self.agent_id = agent_id
        # The build mode. Valid values:
        # 
        # - `0`: prompt-based mode.
        # 
        # - `1`: dialog flow mode.
        self.agent_mode = agent_mode
        # The agent name.
        self.agent_name = agent_name
        # The deployment status. Valid values:
        # 
        # - `0`: Inactive (NOT_EFFECT).
        # 
        # - `1`: Active (EFFECT).
        self.branch_deploy_status = branch_deploy_status
        # The branch description.
        self.branch_desc = branch_desc
        # The branch ID.
        self.branch_id = branch_id
        # The branch name.
        self.branch_name = branch_name
        # The knowledge base configuration.
        self.knowledge_config = knowledge_config
        # The call variable configuration.
        self.phone_tag_config = phone_tag_config
        # The scenario.
        self.scene = scene
        # The call summary configuration.
        self.summary_config = summary_config
        # Version Description
        self.version_desc = version_desc
        # Version ID.
        self.version_id = version_id
        # Version name.
        self.version_name = version_name
        # The release status of the version. 0 indicates Unreleased, 1 indicates Released, and 2 indicates Draft.
        self.version_publish_status = version_publish_status
        # The most recent release time of the version.
        self.version_publish_time = version_publish_time

    def validate(self):
        if self.agent_call_config:
            self.agent_call_config.validate()
        if self.agent_demand_config:
            self.agent_demand_config.validate()
        if self.knowledge_config:
            self.knowledge_config.validate()
        if self.phone_tag_config:
            for v1 in self.phone_tag_config:
                 if v1:
                    v1.validate()
        if self.summary_config:
            self.summary_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_call_config is not None:
            result['AgentCallConfig'] = self.agent_call_config.to_map()

        if self.agent_demand_config is not None:
            result['AgentDemandConfig'] = self.agent_demand_config.to_map()

        if self.agent_desc is not None:
            result['AgentDesc'] = self.agent_desc

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_mode is not None:
            result['AgentMode'] = self.agent_mode

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.branch_deploy_status is not None:
            result['BranchDeployStatus'] = self.branch_deploy_status

        if self.branch_desc is not None:
            result['BranchDesc'] = self.branch_desc

        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.knowledge_config is not None:
            result['KnowledgeConfig'] = self.knowledge_config.to_map()

        result['PhoneTagConfig'] = []
        if self.phone_tag_config is not None:
            for k1 in self.phone_tag_config:
                result['PhoneTagConfig'].append(k1.to_map() if k1 else None)

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.summary_config is not None:
            result['SummaryConfig'] = self.summary_config.to_map()

        if self.version_desc is not None:
            result['VersionDesc'] = self.version_desc

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.version_publish_status is not None:
            result['VersionPublishStatus'] = self.version_publish_status

        if self.version_publish_time is not None:
            result['VersionPublishTime'] = self.version_publish_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentCallConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfig()
            self.agent_call_config = temp_model.from_map(m.get('AgentCallConfig'))

        if m.get('AgentDemandConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentDemandConfig()
            self.agent_demand_config = temp_model.from_map(m.get('AgentDemandConfig'))

        if m.get('AgentDesc') is not None:
            self.agent_desc = m.get('AgentDesc')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentMode') is not None:
            self.agent_mode = m.get('AgentMode')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('BranchDeployStatus') is not None:
            self.branch_deploy_status = m.get('BranchDeployStatus')

        if m.get('BranchDesc') is not None:
            self.branch_desc = m.get('BranchDesc')

        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('KnowledgeConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataKnowledgeConfig()
            self.knowledge_config = temp_model.from_map(m.get('KnowledgeConfig'))

        self.phone_tag_config = []
        if m.get('PhoneTagConfig') is not None:
            for k1 in m.get('PhoneTagConfig'):
                temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataPhoneTagConfig()
                self.phone_tag_config.append(temp_model.from_map(k1))

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('SummaryConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfig()
            self.summary_config = temp_model.from_map(m.get('SummaryConfig'))

        if m.get('VersionDesc') is not None:
            self.version_desc = m.get('VersionDesc')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        if m.get('VersionPublishStatus') is not None:
            self.version_publish_status = m.get('VersionPublishStatus')

        if m.get('VersionPublishTime') is not None:
            self.version_publish_time = m.get('VersionPublishTime')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfig(DaraModel):
    def __init__(
        self,
        call_result_tag_config: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigCallResultTagConfig = None,
        main_purpose: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigMainPurpose = None,
        output_tag_config: List[main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigOutputTagConfig] = None,
    ):
        # The configuration for mapping call results to tags.
        self.call_result_tag_config = call_result_tag_config
        # The main intent.
        self.main_purpose = main_purpose
        # The output tag configuration.
        self.output_tag_config = output_tag_config

    def validate(self):
        if self.call_result_tag_config:
            self.call_result_tag_config.validate()
        if self.main_purpose:
            self.main_purpose.validate()
        if self.output_tag_config:
            for v1 in self.output_tag_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_result_tag_config is not None:
            result['CallResultTagConfig'] = self.call_result_tag_config.to_map()

        if self.main_purpose is not None:
            result['MainPurpose'] = self.main_purpose.to_map()

        result['OutputTagConfig'] = []
        if self.output_tag_config is not None:
            for k1 in self.output_tag_config:
                result['OutputTagConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallResultTagConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigCallResultTagConfig()
            self.call_result_tag_config = temp_model.from_map(m.get('CallResultTagConfig'))

        if m.get('MainPurpose') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigMainPurpose()
            self.main_purpose = temp_model.from_map(m.get('MainPurpose'))

        self.output_tag_config = []
        if m.get('OutputTagConfig') is not None:
            for k1 in m.get('OutputTagConfig'):
                temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigOutputTagConfig()
                self.output_tag_config.append(temp_model.from_map(k1))

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigOutputTagConfig(DaraModel):
    def __init__(
        self,
        id: str = None,
        output_tag_description: str = None,
        output_tag_enum: List[main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigOutputTagConfigOutputTagEnum] = None,
        output_tag_name: str = None,
        output_tag_type: str = None,
    ):
        # The ID of the output tag.
        self.id = id
        # The description of the output tag.
        self.output_tag_description = output_tag_description
        # The enumerated values for the output tag.
        self.output_tag_enum = output_tag_enum
        # The name of the output tag.
        self.output_tag_name = output_tag_name
        # The value type of the output tag. Valid values: `TEXT` and `ENUM`.
        self.output_tag_type = output_tag_type

    def validate(self):
        if self.output_tag_enum:
            for v1 in self.output_tag_enum:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.output_tag_description is not None:
            result['OutputTagDescription'] = self.output_tag_description

        result['OutputTagEnum'] = []
        if self.output_tag_enum is not None:
            for k1 in self.output_tag_enum:
                result['OutputTagEnum'].append(k1.to_map() if k1 else None)

        if self.output_tag_name is not None:
            result['OutputTagName'] = self.output_tag_name

        if self.output_tag_type is not None:
            result['OutputTagType'] = self.output_tag_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OutputTagDescription') is not None:
            self.output_tag_description = m.get('OutputTagDescription')

        self.output_tag_enum = []
        if m.get('OutputTagEnum') is not None:
            for k1 in m.get('OutputTagEnum'):
                temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigOutputTagConfigOutputTagEnum()
                self.output_tag_enum.append(temp_model.from_map(k1))

        if m.get('OutputTagName') is not None:
            self.output_tag_name = m.get('OutputTagName')

        if m.get('OutputTagType') is not None:
            self.output_tag_type = m.get('OutputTagType')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigOutputTagConfigOutputTagEnum(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        value: str = None,
    ):
        # The tag description.
        self.description = description
        # The tag ID.
        self.id = id
        # The enumerated value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigMainPurpose(DaraModel):
    def __init__(
        self,
        id: str = None,
        main_purpose_description: str = None,
        main_purpose_enum: List[main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigMainPurposeMainPurposeEnum] = None,
        main_purpose_name: str = None,
        main_purpose_type: str = None,
    ):
        # The ID of the main intent.
        self.id = id
        # The description of the main intent.
        self.main_purpose_description = main_purpose_description
        # The enumerated values for the main intent.
        self.main_purpose_enum = main_purpose_enum
        # The name of the main intent.
        self.main_purpose_name = main_purpose_name
        # The value type of the main intent. Valid values: `TEXT` and `ENUM`.
        self.main_purpose_type = main_purpose_type

    def validate(self):
        if self.main_purpose_enum:
            for v1 in self.main_purpose_enum:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.main_purpose_description is not None:
            result['MainPurposeDescription'] = self.main_purpose_description

        result['MainPurposeEnum'] = []
        if self.main_purpose_enum is not None:
            for k1 in self.main_purpose_enum:
                result['MainPurposeEnum'].append(k1.to_map() if k1 else None)

        if self.main_purpose_name is not None:
            result['MainPurposeName'] = self.main_purpose_name

        if self.main_purpose_type is not None:
            result['MainPurposeType'] = self.main_purpose_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MainPurposeDescription') is not None:
            self.main_purpose_description = m.get('MainPurposeDescription')

        self.main_purpose_enum = []
        if m.get('MainPurposeEnum') is not None:
            for k1 in m.get('MainPurposeEnum'):
                temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigMainPurposeMainPurposeEnum()
                self.main_purpose_enum.append(temp_model.from_map(k1))

        if m.get('MainPurposeName') is not None:
            self.main_purpose_name = m.get('MainPurposeName')

        if m.get('MainPurposeType') is not None:
            self.main_purpose_type = m.get('MainPurposeType')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigMainPurposeMainPurposeEnum(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        value: str = None,
    ):
        # The description of the value.
        self.description = description
        # The unique ID of the tag.
        self.id = id
        # The value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigCallResultTagConfig(DaraModel):
    def __init__(
        self,
        default_tag: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigCallResultTagConfigDefaultTag = None,
        mapping_tag: Dict[str, str] = None,
    ):
        # The default fallback tag information.
        self.default_tag = default_tag
        # The mapping of call results to tags.
        self.mapping_tag = mapping_tag

    def validate(self):
        if self.default_tag:
            self.default_tag.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_tag is not None:
            result['DefaultTag'] = self.default_tag.to_map()

        if self.mapping_tag is not None:
            result['MappingTag'] = self.mapping_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultTag') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigCallResultTagConfigDefaultTag()
            self.default_tag = temp_model.from_map(m.get('DefaultTag'))

        if m.get('MappingTag') is not None:
            self.mapping_tag = m.get('MappingTag')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataSummaryConfigCallResultTagConfigDefaultTag(DaraModel):
    def __init__(
        self,
        desc: str = None,
        tag: str = None,
    ):
        # The description.
        self.desc = desc
        # The tag.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataPhoneTagConfig(DaraModel):
    def __init__(
        self,
        id: str = None,
        phone_tag_enum: List[main_models.QueryAiVoiceAgentDetailNewResponseBodyDataPhoneTagConfigPhoneTagEnum] = None,
        phone_tag_key: str = None,
        phone_tag_name: str = None,
        phone_tag_required: bool = None,
        phone_tag_source: str = None,
        phone_tag_type: str = None,
    ):
        # The ID of the call variable.
        self.id = id
        # The enumerated values for the call variable.
        self.phone_tag_enum = phone_tag_enum
        # The key of the call variable.
        self.phone_tag_key = phone_tag_key
        # The description of the call variable.
        self.phone_tag_name = phone_tag_name
        # Specifies whether the call variable is required.
        self.phone_tag_required = phone_tag_required
        # The source of the call variable.
        self.phone_tag_source = phone_tag_source
        # The type of the call variable. Valid values: `TEXT` and `ENUM`.
        self.phone_tag_type = phone_tag_type

    def validate(self):
        if self.phone_tag_enum:
            for v1 in self.phone_tag_enum:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        result['PhoneTagEnum'] = []
        if self.phone_tag_enum is not None:
            for k1 in self.phone_tag_enum:
                result['PhoneTagEnum'].append(k1.to_map() if k1 else None)

        if self.phone_tag_key is not None:
            result['PhoneTagKey'] = self.phone_tag_key

        if self.phone_tag_name is not None:
            result['PhoneTagName'] = self.phone_tag_name

        if self.phone_tag_required is not None:
            result['PhoneTagRequired'] = self.phone_tag_required

        if self.phone_tag_source is not None:
            result['PhoneTagSource'] = self.phone_tag_source

        if self.phone_tag_type is not None:
            result['PhoneTagType'] = self.phone_tag_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.phone_tag_enum = []
        if m.get('PhoneTagEnum') is not None:
            for k1 in m.get('PhoneTagEnum'):
                temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataPhoneTagConfigPhoneTagEnum()
                self.phone_tag_enum.append(temp_model.from_map(k1))

        if m.get('PhoneTagKey') is not None:
            self.phone_tag_key = m.get('PhoneTagKey')

        if m.get('PhoneTagName') is not None:
            self.phone_tag_name = m.get('PhoneTagName')

        if m.get('PhoneTagRequired') is not None:
            self.phone_tag_required = m.get('PhoneTagRequired')

        if m.get('PhoneTagSource') is not None:
            self.phone_tag_source = m.get('PhoneTagSource')

        if m.get('PhoneTagType') is not None:
            self.phone_tag_type = m.get('PhoneTagType')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataPhoneTagConfigPhoneTagEnum(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: str = None,
        value: str = None,
    ):
        # The description.
        self.description = description
        # The tag ID.
        self.id = id
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataKnowledgeConfig(DaraModel):
    def __init__(
        self,
        knowledge_ids: List[main_models.QueryAiVoiceAgentDetailNewResponseBodyDataKnowledgeConfigKnowledgeIds] = None,
        rag_config: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataKnowledgeConfigRagConfig = None,
    ):
        # The collection of knowledge bases.
        self.knowledge_ids = knowledge_ids
        # The Retrieval-Augmented Generation (RAG) configuration.
        self.rag_config = rag_config

    def validate(self):
        if self.knowledge_ids:
            for v1 in self.knowledge_ids:
                 if v1:
                    v1.validate()
        if self.rag_config:
            self.rag_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgeIds'] = []
        if self.knowledge_ids is not None:
            for k1 in self.knowledge_ids:
                result['KnowledgeIds'].append(k1.to_map() if k1 else None)

        if self.rag_config is not None:
            result['RagConfig'] = self.rag_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_ids = []
        if m.get('KnowledgeIds') is not None:
            for k1 in m.get('KnowledgeIds'):
                temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataKnowledgeConfigKnowledgeIds()
                self.knowledge_ids.append(temp_model.from_map(k1))

        if m.get('RagConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataKnowledgeConfigRagConfig()
            self.rag_config = temp_model.from_map(m.get('RagConfig'))

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataKnowledgeConfigRagConfig(DaraModel):
    def __init__(
        self,
        description: str = None,
        enabled: bool = None,
    ):
        # RAG retrieval description
        self.description = description
        # Enable RAG retrieval
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataKnowledgeConfigKnowledgeIds(DaraModel):
    def __init__(
        self,
        knowledge_id: int = None,
        knowledge_name: str = None,
    ):
        # The ID of the knowledge base.
        self.knowledge_id = knowledge_id
        # The name of the knowledge base.
        self.knowledge_name = knowledge_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.knowledge_name is not None:
            result['KnowledgeName'] = self.knowledge_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('KnowledgeName') is not None:
            self.knowledge_name = m.get('KnowledgeName')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataAgentDemandConfig(DaraModel):
    def __init__(
        self,
        ai_generate: bool = None,
        basic_task_description: str = None,
        business_type: int = None,
        core_target: str = None,
        sys_role: str = None,
        user_role: str = None,
    ):
        # Specifies whether the agent was built with AI assistance.
        self.ai_generate = ai_generate
        # The basic task configuration.
        self.basic_task_description = basic_task_description
        # The business scenario.
        self.business_type = business_type
        # The core objective.
        self.core_target = core_target
        # The system role.
        self.sys_role = sys_role
        # The user role.
        self.user_role = user_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_generate is not None:
            result['AiGenerate'] = self.ai_generate

        if self.basic_task_description is not None:
            result['BasicTaskDescription'] = self.basic_task_description

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.core_target is not None:
            result['CoreTarget'] = self.core_target

        if self.sys_role is not None:
            result['SysRole'] = self.sys_role

        if self.user_role is not None:
            result['UserRole'] = self.user_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiGenerate') is not None:
            self.ai_generate = m.get('AiGenerate')

        if m.get('BasicTaskDescription') is not None:
            self.basic_task_description = m.get('BasicTaskDescription')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CoreTarget') is not None:
            self.core_target = m.get('CoreTarget')

        if m.get('SysRole') is not None:
            self.sys_role = m.get('SysRole')

        if m.get('UserRole') is not None:
            self.user_role = m.get('UserRole')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfig(DaraModel):
    def __init__(
        self,
        event_config: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfigEventConfig = None,
        prologue: str = None,
        recording_file: str = None,
        start_word_type: int = None,
        transfer_config: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfigTransferConfig = None,
        tts_config: main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfigTtsConfig = None,
        vocab_id: str = None,
    ):
        # The event configuration.
        self.event_config = event_config
        # The prologue.
        self.prologue = prologue
        # The URL of the audio file for the prologue. This parameter is returned only when `StartWordType` is set to `1`.
        self.recording_file = recording_file
        # The type of the prologue. Valid values: `0` (text) and `1` (recording).
        self.start_word_type = start_word_type
        # The configuration for transferring the call to a manual agent.
        self.transfer_config = transfer_config
        # The Text-to-Speech (TTS) configuration.
        self.tts_config = tts_config
        # The ID of the hotword vocabulary.
        self.vocab_id = vocab_id

    def validate(self):
        if self.event_config:
            self.event_config.validate()
        if self.transfer_config:
            self.transfer_config.validate()
        if self.tts_config:
            self.tts_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_config is not None:
            result['EventConfig'] = self.event_config.to_map()

        if self.prologue is not None:
            result['Prologue'] = self.prologue

        if self.recording_file is not None:
            result['RecordingFile'] = self.recording_file

        if self.start_word_type is not None:
            result['StartWordType'] = self.start_word_type

        if self.transfer_config is not None:
            result['TransferConfig'] = self.transfer_config.to_map()

        if self.tts_config is not None:
            result['TtsConfig'] = self.tts_config.to_map()

        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfigEventConfig()
            self.event_config = temp_model.from_map(m.get('EventConfig'))

        if m.get('Prologue') is not None:
            self.prologue = m.get('Prologue')

        if m.get('RecordingFile') is not None:
            self.recording_file = m.get('RecordingFile')

        if m.get('StartWordType') is not None:
            self.start_word_type = m.get('StartWordType')

        if m.get('TransferConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfigTransferConfig()
            self.transfer_config = temp_model.from_map(m.get('TransferConfig'))

        if m.get('TtsConfig') is not None:
            temp_model = main_models.QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfigTtsConfig()
            self.tts_config = temp_model.from_map(m.get('TtsConfig'))

        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfigTtsConfig(DaraModel):
    def __init__(
        self,
        background_enabled: bool = None,
        background_sound: int = None,
        background_volume: int = None,
        customer_account_id: int = None,
        mixing_enabled: bool = None,
        mixing_template: int = None,
        resource_id: str = None,
        tts_speed: int = None,
        tts_style: str = None,
        tts_volume: int = None,
        voice_code: str = None,
        voice_type: bool = None,
    ):
        # Specifies whether to enable background sound.
        self.background_enabled = background_enabled
        # The ID of the background sound.
        self.background_sound = background_sound
        # The volume of the background sound. Valid values: `0` (low), `1` (medium), and `2` (high).
        self.background_volume = background_volume
        # The account of the third-party voice platform.
        self.customer_account_id = customer_account_id
        # Specifies whether to enable audio mixing.
        self.mixing_enabled = mixing_enabled
        # The ID of the audio mixing template.
        self.mixing_template = mixing_template
        # The resource ID. This parameter is required only for third-party voices.
        self.resource_id = resource_id
        # The speech rate for TTS playback. Valid values: -200 to 200. Default value: 0.
        self.tts_speed = tts_speed
        # The voice style.
        self.tts_style = tts_style
        # The volume of TTS playback. Valid values: 0 to 100.
        self.tts_volume = tts_volume
        # The voice code.
        self.voice_code = voice_code
        # The type of the TTS voice. Valid values:
        # 
        # `VOICE_TYPE_SYSTEM`: a system voice.
        # 
        # `VOICE_TYPE_CLONE`: a cloned voice.
        # 
        # `VOICE_TYPE_DOUBAO`: a Doubao voice.
        # 
        # `VOICE_TYPE_MINIMAX`: a Minimax voice.
        # 
        # `VOICE_TYPE_OPENTTS`: an open voice.
        # 
        # `VOICE_TYPE_BL_CUSTOM`: a high-quality custom cloned voice.
        self.voice_type = voice_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_enabled is not None:
            result['BackgroundEnabled'] = self.background_enabled

        if self.background_sound is not None:
            result['BackgroundSound'] = self.background_sound

        if self.background_volume is not None:
            result['BackgroundVolume'] = self.background_volume

        if self.customer_account_id is not None:
            result['CustomerAccountId'] = self.customer_account_id

        if self.mixing_enabled is not None:
            result['MixingEnabled'] = self.mixing_enabled

        if self.mixing_template is not None:
            result['MixingTemplate'] = self.mixing_template

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.tts_speed is not None:
            result['TtsSpeed'] = self.tts_speed

        if self.tts_style is not None:
            result['TtsStyle'] = self.tts_style

        if self.tts_volume is not None:
            result['TtsVolume'] = self.tts_volume

        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code

        if self.voice_type is not None:
            result['VoiceType'] = self.voice_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundEnabled') is not None:
            self.background_enabled = m.get('BackgroundEnabled')

        if m.get('BackgroundSound') is not None:
            self.background_sound = m.get('BackgroundSound')

        if m.get('BackgroundVolume') is not None:
            self.background_volume = m.get('BackgroundVolume')

        if m.get('CustomerAccountId') is not None:
            self.customer_account_id = m.get('CustomerAccountId')

        if m.get('MixingEnabled') is not None:
            self.mixing_enabled = m.get('MixingEnabled')

        if m.get('MixingTemplate') is not None:
            self.mixing_template = m.get('MixingTemplate')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')

        if m.get('TtsStyle') is not None:
            self.tts_style = m.get('TtsStyle')

        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')

        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')

        if m.get('VoiceType') is not None:
            self.voice_type = m.get('VoiceType')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfigTransferConfig(DaraModel):
    def __init__(
        self,
        called_number: str = None,
        caller_number: str = None,
        caller_number_type: int = None,
        calling_number: str = None,
        calling_number_type: int = None,
        customer_route_code: str = None,
        enabled: bool = None,
        extra_info: str = None,
        failure_content: str = None,
        seat_route_code: str = None,
        seat_route_name: str = None,
        transfer_biz_id: str = None,
        transfer_content: str = None,
        transfer_type: int = None,
    ):
        # The called number.
        self.called_number = called_number
        # The caller number.
        self.caller_number = caller_number
        # The type of the caller number.
        self.caller_number_type = caller_number_type
        # The destination number for the transfer, such as the phone number of a customer service agent.
        self.calling_number = calling_number
        # The type of the called number.
        self.calling_number_type = calling_number_type
        # The customer route code.
        self.customer_route_code = customer_route_code
        # Specifies whether to enable call transfer.
        self.enabled = enabled
        # The supplementary information.
        self.extra_info = extra_info
        # The prompt that is played when the transfer to a manual agent fails.
        self.failure_content = failure_content
        # The agent route code.
        self.seat_route_code = seat_route_code
        # The name of the agent route.
        self.seat_route_name = seat_route_name
        # The business ID.
        self.transfer_biz_id = transfer_biz_id
        # The prompt that is played when the call is transferred to a manual agent.
        self.transfer_content = transfer_content
        # The agent transfer type.
        self.transfer_type = transfer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.caller_number_type is not None:
            result['CallerNumberType'] = self.caller_number_type

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.calling_number_type is not None:
            result['CallingNumberType'] = self.calling_number_type

        if self.customer_route_code is not None:
            result['CustomerRouteCode'] = self.customer_route_code

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.failure_content is not None:
            result['FailureContent'] = self.failure_content

        if self.seat_route_code is not None:
            result['SeatRouteCode'] = self.seat_route_code

        if self.seat_route_name is not None:
            result['SeatRouteName'] = self.seat_route_name

        if self.transfer_biz_id is not None:
            result['TransferBizId'] = self.transfer_biz_id

        if self.transfer_content is not None:
            result['TransferContent'] = self.transfer_content

        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('CallerNumberType') is not None:
            self.caller_number_type = m.get('CallerNumberType')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('CallingNumberType') is not None:
            self.calling_number_type = m.get('CallingNumberType')

        if m.get('CustomerRouteCode') is not None:
            self.customer_route_code = m.get('CustomerRouteCode')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('FailureContent') is not None:
            self.failure_content = m.get('FailureContent')

        if m.get('SeatRouteCode') is not None:
            self.seat_route_code = m.get('SeatRouteCode')

        if m.get('SeatRouteName') is not None:
            self.seat_route_name = m.get('SeatRouteName')

        if m.get('TransferBizId') is not None:
            self.transfer_biz_id = m.get('TransferBizId')

        if m.get('TransferContent') is not None:
            self.transfer_content = m.get('TransferContent')

        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')

        return self

class QueryAiVoiceAgentDetailNewResponseBodyDataAgentCallConfigEventConfig(DaraModel):
    def __init__(
        self,
        call_assistant_hangup: bool = None,
        call_assistant_recognize: bool = None,
        mute_active: bool = None,
        mute_duration: int = None,
        mute_hangup_num: int = None,
        session_timeout: int = None,
    ):
        # Specifies whether to disconnect the call when an answering machine is detected.
        self.call_assistant_hangup = call_assistant_hangup
        # Specifies whether to enable answering machine detection.
        self.call_assistant_recognize = call_assistant_recognize
        # Specifies whether to wake up the model upon the first mute event.
        self.mute_active = mute_active
        # The mute duration. Unit: seconds. Valid values: 3 to 15.
        self.mute_duration = mute_duration
        # The number of consecutive mute events that trigger an automatic disconnection. Valid values: 1 to 5.
        self.mute_hangup_num = mute_hangup_num
        # The maximum call duration. Unit: seconds. Valid values: 600 to 3600. The call is automatically disconnected if this duration is exceeded.
        self.session_timeout = session_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_assistant_hangup is not None:
            result['CallAssistantHangup'] = self.call_assistant_hangup

        if self.call_assistant_recognize is not None:
            result['CallAssistantRecognize'] = self.call_assistant_recognize

        if self.mute_active is not None:
            result['MuteActive'] = self.mute_active

        if self.mute_duration is not None:
            result['MuteDuration'] = self.mute_duration

        if self.mute_hangup_num is not None:
            result['MuteHangupNum'] = self.mute_hangup_num

        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallAssistantHangup') is not None:
            self.call_assistant_hangup = m.get('CallAssistantHangup')

        if m.get('CallAssistantRecognize') is not None:
            self.call_assistant_recognize = m.get('CallAssistantRecognize')

        if m.get('MuteActive') is not None:
            self.mute_active = m.get('MuteActive')

        if m.get('MuteDuration') is not None:
            self.mute_duration = m.get('MuteDuration')

        if m.get('MuteHangupNum') is not None:
            self.mute_hangup_num = m.get('MuteHangupNum')

        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')

        return self

