# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CreateScheduledTaskRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        description: List[main_models.CreateScheduledTaskRequestDescription] = None,
        digital_employee_name: List[str] = None,
        is_open: bool = None,
        model: str = None,
        name: str = None,
        segments: List[main_models.CreateScheduledTaskRequestSegments] = None,
        task_detail: main_models.CreateScheduledTaskRequestTaskDetail = None,
        tenant_id: str = None,
        trigger_config: main_models.CreateScheduledTaskRequestTriggerConfig = None,
        visibility: str = None,
        visible_member_user_ids: List[str] = None,
    ):
        # The ID of the collaboration group (such as cg_101). If specified, a group space task is created (the caller must be a valid group member). If empty, a personal task is created.
        self.collaboration_group_id = collaboration_group_id
        # The description of the to-do card type.
        self.description = description
        # The name of the current effective digital employee. This parameter is empty if not configured.
        self.digital_employee_name = digital_employee_name
        # Specifies whether public access is enabled.
        self.is_open = is_open
        # The large model used by the assistant. An empty value indicates that DingTalk automatically selects the model.
        self.model = model
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The site ID.
        self.segments = segments
        # The task details.
        self.task_detail = task_detail
        # The ID of the effective tenant.
        self.tenant_id = tenant_id
        # The trigger configuration. The configuration varies depending on the trigger type. For the specific format, refer to the following data structures:
        # 
        #   - OSS trigger: See [OSSTriggerConfig](https://help.aliyun.com/document_detail/415697.html).
        #   - Simple Log Service trigger: See [LogTriggerConfig](https://help.aliyun.com/document_detail/415694.html).
        #   - Time trigger: See [TimeTriggerConfig](https://help.aliyun.com/document_detail/415712.html).
        #   - HTTP trigger: See [HTTPTriggerConfig](https://help.aliyun.com/document_detail/415685.html).
        #   - Tablestore trigger: You only need to specify the complete **SourceArn** parameter. No additional configuration is required. Set the value to an empty object {}.
        #   - CDN event trigger: See [CDNEventsTriggerConfig](https://help.aliyun.com/document_detail/415674.html).
        #   - MNS topic trigger: See [MnsTopicTriggerConfig](https://help.aliyun.com/document_detail/415695.html).
        #   - EventBridge trigger: See [EventBridgeTriggerConfig](https://help.aliyun.com/document_detail/2508622.html).
        self.trigger_config = trigger_config
        # The visibility scope of the group task. Valid values: PRIVATE (visible only to the creator and group owner), COLLABORATIVE (visible to specified collaborators), and PUBLIC (visible to all group members). Default value for group tasks: PRIVATE. This parameter is ignored for personal tasks.
        self.visibility = visibility
        # The list of collaborator user IDs. This parameter takes effect only when visibility is set to COLLABORATIVE. It is ignored for other visibility levels. A maximum of 1000 IDs are supported. The task creator and group creator do not need to be included (covered by the authentication layer). This parameter is ignored for personal tasks.
        self.visible_member_user_ids = visible_member_user_ids

    def validate(self):
        if self.description:
            for v1 in self.description:
                 if v1:
                    v1.validate()
        if self.segments:
            for v1 in self.segments:
                 if v1:
                    v1.validate()
        if self.task_detail:
            self.task_detail.validate()
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        result['description'] = []
        if self.description is not None:
            for k1 in self.description:
                result['description'].append(k1.to_map() if k1 else None)

        if self.digital_employee_name is not None:
            result['digitalEmployeeName'] = self.digital_employee_name

        if self.is_open is not None:
            result['isOpen'] = self.is_open

        if self.model is not None:
            result['model'] = self.model

        if self.name is not None:
            result['name'] = self.name

        result['segments'] = []
        if self.segments is not None:
            for k1 in self.segments:
                result['segments'].append(k1.to_map() if k1 else None)

        if self.task_detail is not None:
            result['taskDetail'] = self.task_detail.to_map()

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.trigger_config is not None:
            result['triggerConfig'] = self.trigger_config.to_map()

        if self.visibility is not None:
            result['visibility'] = self.visibility

        if self.visible_member_user_ids is not None:
            result['visibleMemberUserIds'] = self.visible_member_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        self.description = []
        if m.get('description') is not None:
            for k1 in m.get('description'):
                temp_model = main_models.CreateScheduledTaskRequestDescription()
                self.description.append(temp_model.from_map(k1))

        if m.get('digitalEmployeeName') is not None:
            self.digital_employee_name = m.get('digitalEmployeeName')

        if m.get('isOpen') is not None:
            self.is_open = m.get('isOpen')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.segments = []
        if m.get('segments') is not None:
            for k1 in m.get('segments'):
                temp_model = main_models.CreateScheduledTaskRequestSegments()
                self.segments.append(temp_model.from_map(k1))

        if m.get('taskDetail') is not None:
            temp_model = main_models.CreateScheduledTaskRequestTaskDetail()
            self.task_detail = temp_model.from_map(m.get('taskDetail'))

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('triggerConfig') is not None:
            temp_model = main_models.CreateScheduledTaskRequestTriggerConfig()
            self.trigger_config = temp_model.from_map(m.get('triggerConfig'))

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        if m.get('visibleMemberUserIds') is not None:
            self.visible_member_user_ids = m.get('visibleMemberUserIds')

        return self

class CreateScheduledTaskRequestTriggerConfig(DaraModel):
    def __init__(
        self,
        cron: str = None,
        language: str = None,
        push_config: List[main_models.CreateScheduledTaskRequestTriggerConfigPushConfig] = None,
        timezone: str = None,
        trigger_mode: str = None,
    ):
        # The periodic training information in cron syntax (Minutes Hours DayofMonth Month DayofWeek). An empty value indicates that periodic training is not performed (default). In DayofWeek, 0 indicates Sunday.
        self.cron = cron
        # The language. Valid values:
        # 
        # - zh_CN: Chinese (default)
        # - en_US: English
        self.language = language
        # The list of task push channels. No push is performed if the list is empty or no channel is enabled.
        self.push_config = push_config
        # The time zone.
        self.timezone = timezone
        # The trigger mode.
        #  
        #   1: Manual trigger
        #    
        #   2: Scheduled trigger 
        # 
        #   3: Code commit trigger
        #  
        #   5: Pipeline trigger
        # 
        #   6: WEBHOOK trigger
        self.trigger_mode = trigger_mode

    def validate(self):
        if self.push_config:
            for v1 in self.push_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['cron'] = self.cron

        if self.language is not None:
            result['language'] = self.language

        result['pushConfig'] = []
        if self.push_config is not None:
            for k1 in self.push_config:
                result['pushConfig'].append(k1.to_map() if k1 else None)

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.trigger_mode is not None:
            result['triggerMode'] = self.trigger_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cron') is not None:
            self.cron = m.get('cron')

        if m.get('language') is not None:
            self.language = m.get('language')

        self.push_config = []
        if m.get('pushConfig') is not None:
            for k1 in m.get('pushConfig'):
                temp_model = main_models.CreateScheduledTaskRequestTriggerConfigPushConfig()
                self.push_config.append(temp_model.from_map(k1))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('triggerMode') is not None:
            self.trigger_mode = m.get('triggerMode')

        return self

class CreateScheduledTaskRequestTriggerConfigPushConfig(DaraModel):
    def __init__(
        self,
        channel_type: str = None,
        content_scope: str = None,
        delivery_method: str = None,
        enabled: bool = None,
        file_format: str = None,
        operating_object_name: str = None,
        receiver_type: str = None,
    ):
        # The notification method. Valid values:
        # 
        # - **hdm_alarm_sms**: SMS.
        # - **dingtalk**: DingTalk chatbot.
        # - **hdm_alarm_sms_and_email**: SMS and email.
        # - **hdm_alarm_sms,dingtalk**: SMS and DingTalk chatbot.
        self.channel_type = channel_type
        # The push content scope. Default value: all_replies.
        self.content_scope = content_scope
        # The push method. Default value: channel_bot.
        self.delivery_method = delivery_method
        # Specifies whether the credential is enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.enabled = enabled
        # The file format. Valid values: Excel and CSV.
        self.file_format = file_format
        # The digital employee name (operating object name, optional).
        self.operating_object_name = operating_object_name
        # The file receiver type. Valid values:
        # 
        # - 0: One-on-one chat.
        # 
        # - 1: Group chat.
        # 
        # - 2: DingTalk Drive.
        # 
        # - 3: Document.
        self.receiver_type = receiver_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_type is not None:
            result['channelType'] = self.channel_type

        if self.content_scope is not None:
            result['contentScope'] = self.content_scope

        if self.delivery_method is not None:
            result['deliveryMethod'] = self.delivery_method

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.file_format is not None:
            result['fileFormat'] = self.file_format

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.receiver_type is not None:
            result['receiverType'] = self.receiver_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')

        if m.get('contentScope') is not None:
            self.content_scope = m.get('contentScope')

        if m.get('deliveryMethod') is not None:
            self.delivery_method = m.get('deliveryMethod')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('fileFormat') is not None:
            self.file_format = m.get('fileFormat')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('receiverType') is not None:
            self.receiver_type = m.get('receiverType')

        return self

class CreateScheduledTaskRequestTaskDetail(DaraModel):
    def __init__(
        self,
        related_objects: List[main_models.CreateScheduledTaskRequestTaskDetailRelatedObjects] = None,
        related_semantics: List[main_models.CreateScheduledTaskRequestTaskDetailRelatedSemantics] = None,
        related_skills: List[main_models.CreateScheduledTaskRequestTaskDetailRelatedSkills] = None,
        task_understand: str = None,
    ):
        # The related objects.
        self.related_objects = related_objects
        # The related semantics.
        self.related_semantics = related_semantics
        # The related skills.
        self.related_skills = related_skills
        # The task understanding description polished by the LLM.
        self.task_understand = task_understand

    def validate(self):
        if self.related_objects:
            for v1 in self.related_objects:
                 if v1:
                    v1.validate()
        if self.related_semantics:
            for v1 in self.related_semantics:
                 if v1:
                    v1.validate()
        if self.related_skills:
            for v1 in self.related_skills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['relatedObjects'] = []
        if self.related_objects is not None:
            for k1 in self.related_objects:
                result['relatedObjects'].append(k1.to_map() if k1 else None)

        result['relatedSemantics'] = []
        if self.related_semantics is not None:
            for k1 in self.related_semantics:
                result['relatedSemantics'].append(k1.to_map() if k1 else None)

        result['relatedSkills'] = []
        if self.related_skills is not None:
            for k1 in self.related_skills:
                result['relatedSkills'].append(k1.to_map() if k1 else None)

        if self.task_understand is not None:
            result['taskUnderstand'] = self.task_understand

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.related_objects = []
        if m.get('relatedObjects') is not None:
            for k1 in m.get('relatedObjects'):
                temp_model = main_models.CreateScheduledTaskRequestTaskDetailRelatedObjects()
                self.related_objects.append(temp_model.from_map(k1))

        self.related_semantics = []
        if m.get('relatedSemantics') is not None:
            for k1 in m.get('relatedSemantics'):
                temp_model = main_models.CreateScheduledTaskRequestTaskDetailRelatedSemantics()
                self.related_semantics.append(temp_model.from_map(k1))

        self.related_skills = []
        if m.get('relatedSkills') is not None:
            for k1 in m.get('relatedSkills'):
                temp_model = main_models.CreateScheduledTaskRequestTaskDetailRelatedSkills()
                self.related_skills.append(temp_model.from_map(k1))

        if m.get('taskUnderstand') is not None:
            self.task_understand = m.get('taskUnderstand')

        return self

class CreateScheduledTaskRequestTaskDetailRelatedSkills(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        name: str = None,
        skill_code: str = None,
        source_ids: List[str] = None,
    ):
        # The display name.
        self.display_name = display_name
        # The name.
        self.name = name
        # The skill code.
        self.skill_code = skill_code
        # sourceIds
        self.source_ids = source_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.name is not None:
            result['name'] = self.name

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.source_ids is not None:
            result['sourceIds'] = self.source_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('sourceIds') is not None:
            self.source_ids = m.get('sourceIds')

        return self

class CreateScheduledTaskRequestTaskDetailRelatedSemantics(DaraModel):
    def __init__(
        self,
        attributes: str = None,
        entity: str = None,
    ):
        # The file extension information.
        self.attributes = attributes
        # The semantic entity name, such as customer or opportunity.
        self.entity = entity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.entity is not None:
            result['entity'] = self.entity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('entity') is not None:
            self.entity = m.get('entity')

        return self

class CreateScheduledTaskRequestTaskDetailRelatedObjects(DaraModel):
    def __init__(
        self,
        mention_type: str = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
    ):
        # The mention type, such as objects.
        self.mention_type = mention_type
        # The name.
        self.name = name
        # The object ID. Pass the project task ID.
        # 
        # - For internal enterprise applications, use the taskId obtained by calling the [Create a project task](https://open.dingtalk.com/document/orgapp-server/create-a-project-task) operation.
        # 
        # - For third-party enterprise applications, use the taskId obtained by calling the [Create a project task](https://open.dingtalk.com/document/isvapp-server/create-a-project-task) operation.
        self.object_id = object_id
        # The relationship type. Valid values:
        # - crm_customer: enterprise customer.
        # - crm_customer_personal: individual customer.
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mention_type is not None:
            result['mentionType'] = self.mention_type

        if self.name is not None:
            result['name'] = self.name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mentionType') is not None:
            self.mention_type = m.get('mentionType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        return self

class CreateScheduledTaskRequestSegments(DaraModel):
    def __init__(
        self,
        content: str = None,
        enabled: bool = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
        skill_code: str = None,
        type: str = None,
    ):
        # The card callback content.
        self.content = content
        # Specifies whether to enable this feature.
        self.enabled = enabled
        # The name.
        self.name = name
        # The ID of the recommended item, which can be a **feedId** or a micro-application ID.
        self.object_id = object_id
        # The customer type to save.
        self.object_type = object_type
        # The skill code. This parameter has a value when type is set to skill.
        self.skill_code = skill_code
        # The billing type. Only fixed is supported.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.name is not None:
            result['name'] = self.name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class CreateScheduledTaskRequestDescription(DaraModel):
    def __init__(
        self,
        content: str = None,
        enabled: bool = None,
        name: str = None,
        object_id: str = None,
        object_type: str = None,
        skill_code: str = None,
        type: str = None,
    ):
        # The streaming output message.
        self.content = content
        # Specifies whether the throttling rule is enabled. A value of true indicates enabled, and a value of false indicates disabled.
        self.enabled = enabled
        # The name.
        self.name = name
        # The object ID. Pass the project task ID.
        # 
        # - For internal enterprise applications, use the taskId obtained by calling the [Create a project task](https://open.dingtalk.com/document/orgapp-server/create-a-project-task) operation.
        # 
        # - For third-party enterprise applications, use the taskId obtained by calling the [Create a project task](https://open.dingtalk.com/document/isvapp-server/create-a-project-task) operation.
        self.object_id = object_id
        # The object type. Fixed value: task, indicating a project task.
        self.object_type = object_type
        # The skill code. This parameter has a value when type is set to skill.
        self.skill_code = skill_code
        # The HTTP API type. Valid values: Http (standard HTTP API), Rest (RESTful API), WebSocket (WebSocket API), HttpIngress (HTTP API accessed through Ingress), LLM (large language model API), and Agent (Agent proxy API).
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.name is not None:
            result['name'] = self.name

        if self.object_id is not None:
            result['objectId'] = self.object_id

        if self.object_type is not None:
            result['objectType'] = self.object_type

        if self.skill_code is not None:
            result['skillCode'] = self.skill_code

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('objectId') is not None:
            self.object_id = m.get('objectId')

        if m.get('objectType') is not None:
            self.object_type = m.get('objectType')

        if m.get('skillCode') is not None:
            self.skill_code = m.get('skillCode')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

