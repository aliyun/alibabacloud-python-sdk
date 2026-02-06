# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitAIMediaAuditJobRequest(DaraModel):
    def __init__(
        self,
        media_audit_configuration: str = None,
        media_id: str = None,
        media_type: str = None,
        template_id: str = None,
        user_data: str = None,
    ):
        # The configuration information about the review job.
        # 
        # *   Other configuration items of the review job. Only the ResourceType field is supported. This field is used to specify the type of media files. You can adjust review standards and rules based on the type of media files.
        # *   If you want to modify the review standard and rules based on ResourceType, submit a ticket. For more information, see [Contact us](https://help.aliyun.com/document_detail/464625.html).
        # *   The value of ResourceType can contain only letters, digits, and underscores (_).
        self.media_audit_configuration = media_audit_configuration
        # The ID of the video file. To obtain the file ID, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com) and choose **Review Management** > **Content Moderation** in the left-side navigation pane.
        # 
        # This parameter is required.
        self.media_id = media_id
        # The type of the media file. Only **video** is supported.
        self.media_type = media_type
        # The ID of the AI template. You can use one of the following methods to obtain the ID of the AI template:
        # 
        # *   Obtain the value of TemplateId from the response to the [AddAITemplate](https://help.aliyun.com/document_detail/102930.html) operation that you call to create an AI template.
        # *   Obtain the value of TemplateId from the response to the [ListAITemplate](https://help.aliyun.com/document_detail/102936.html) operation that you call to create an AI template.
        # 
        # >  If you do not specify an ID, the ID of the default AI template is used.
        self.template_id = template_id
        # The custom settings. The value must be a JSON string. You can configure settings such as message callbacks. For more information, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        # 
        # >  To use the callback configurations specified by this parameter, you must configure an HTTP callback URL and specify the types of the callback events in the ApsaraVideo VOD console. Otherwise, the callback configurations do not take effect. For more information about how to configure HTTP callback settings in the ApsaraVideo VOD console, see [Configure callback settings](https://help.aliyun.com/document_detail/86071.html).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_audit_configuration is not None:
            result['MediaAuditConfiguration'] = self.media_audit_configuration

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaAuditConfiguration') is not None:
            self.media_audit_configuration = m.get('MediaAuditConfiguration')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

