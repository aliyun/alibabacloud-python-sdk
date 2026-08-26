# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAIMediaAuditJobRequest(DaraModel):
    def __init__(
        self,
        censor_provider: str = None,
        media_audit_configuration: str = None,
        media_id: str = None,
        media_type: str = None,
        service_parameters: str = None,
        template_id: str = None,
        user_data: str = None,
        video_service: str = None,
        voice_service: str = None,
    ):
        self.censor_provider = censor_provider
        # The configuration of the review job.
        # - For other configuration items of the review job, only the ResourceType field is currently supported. This field controls the media file type, and you can adjust the review standards and rules for the specified type.
        # - To adjust the review standards and rules for a ResourceType, submit a ticket for technical support. For information about how to submit a ticket, refer to [Contact us](https://help.aliyun.com/document_detail/464625.html).
        # - Usage notes for ResourceType: Only letters, digits, and underscores (_) are allowed.
        self.media_audit_configuration = media_audit_configuration
        # The audio or video ID. Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Review Management** > **Video Review** to view the audio or video ID.
        # 
        # This parameter is required.
        self.media_id = media_id
        # The media type. Currently, only **video** is supported.
        self.media_type = media_type
        self.service_parameters = service_parameters
        # The AI template ID. You can obtain the ID by using one of the following methods:
        # - When you call the [AddAITemplate](https://help.aliyun.com/document_detail/102930.html) operation to add an AI template, the AI template ID is the value of the TemplateId response parameter.
        # - After the AI template is added, call the [ListAITemplate](https://help.aliyun.com/document_detail/102936.html) operation to query the AI template ID, which is the value of the TemplateId response parameter.
        # 
        # > If you do not specify an AI template ID, the default AI template ID for automated review is used.
        self.template_id = template_id
        # The custom settings. The value is a JSON string that supports settings such as message callbacks. For more information, refer to [UserData](https://help.aliyun.com/document_detail/86952.html).
        # 
        # > To use message callbacks in this parameter, you must configure an HTTP callback URL and select the corresponding callback event types in the console. Otherwise, the callback settings do not take effect. For information about how to configure HTTP callbacks in the console, refer to [Callback settings](https://help.aliyun.com/document_detail/86071.html).
        self.user_data = user_data
        self.video_service = video_service
        self.voice_service = voice_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.censor_provider is not None:
            result['CensorProvider'] = self.censor_provider

        if self.media_audit_configuration is not None:
            result['MediaAuditConfiguration'] = self.media_audit_configuration

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_service is not None:
            result['VideoService'] = self.video_service

        if self.voice_service is not None:
            result['VoiceService'] = self.voice_service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CensorProvider') is not None:
            self.censor_provider = m.get('CensorProvider')

        if m.get('MediaAuditConfiguration') is not None:
            self.media_audit_configuration = m.get('MediaAuditConfiguration')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoService') is not None:
            self.video_service = m.get('VideoService')

        if m.get('VoiceService') is not None:
            self.voice_service = m.get('VoiceService')

        return self

