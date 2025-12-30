# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetEditingProjectResponseBody(DaraModel):
    def __init__(
        self,
        project: main_models.GetEditingProjectResponseBodyProject = None,
        request_id: str = None,
    ):
        # The information about the online editing project.
        self.project = project
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project is not None:
            result['Project'] = self.project.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = main_models.GetEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEditingProjectResponseBodyProject(DaraModel):
    def __init__(
        self,
        business_config: str = None,
        business_status: str = None,
        clips_param: str = None,
        cover_url: str = None,
        create_source: str = None,
        create_time: str = None,
        description: str = None,
        duration: int = None,
        modified_source: str = None,
        modified_time: str = None,
        project_id: str = None,
        project_type: str = None,
        status: str = None,
        template_id: str = None,
        template_type: str = None,
        timeline: str = None,
        timeline_convert_error_message: str = None,
        timeline_convert_status: str = None,
        title: str = None,
    ):
        # The business configuration of the project. This parameter can be ignored for general editing projects.
        self.business_config = business_config
        # The business status of the project. This parameter can be ignored for general editing projects. Valid values:
        # 
        # Reserving
        # 
        # ReservationCanceled
        # 
        # BroadCasting
        # 
        # LoadingFailed
        # 
        # LiveFinished
        self.business_status = business_status
        # The material parameter corresponding to the template, in the JSON format. If TemplateId is specified, ClipsParam must also be specified. For more information<props="china">, see [Create and use a regular template](https://help.aliyun.com/document_detail/328557.html) and [Create and use an advanced template](https://help.aliyun.com/document_detail/291418.html).
        self.clips_param = clips_param
        # The thumbnail URL of the online editing project.
        self.cover_url = cover_url
        # The method for creating the online editing project. Valid values:
        # 
        # \\- OpenAPI
        # 
        # \\- AliyunConsole
        # 
        # \\- WebSDK
        # 
        # \\- LiveEditingOpenAPI
        # 
        # \\- LiveEditingConsole
        self.create_source = create_source
        # The time when the online editing project was created.
        self.create_time = create_time
        # The description of the online editing project.
        self.description = description
        # The total duration of the online editing project.
        self.duration = duration
        # The method for editing the online editing project. Valid values:
        # 
        # \\- OpenAPI
        # 
        # \\- AliyunConsole
        # 
        # \\- WebSDK
        # 
        # \\- LiveEditingOpenAPI
        # 
        # \\- LiveEditingConsole
        self.modified_source = modified_source
        # The time when the online editing project was last modified.
        self.modified_time = modified_time
        # The ID of the online editing project.
        self.project_id = project_id
        # The type of the editing project. Default value: EditingProject. Valid values:
        # 
        # \\- EditingProject: a regular editing project.
        # 
        # \\- LiveEditingProject: a live stream editing project.
        self.project_type = project_type
        # The status of the online editing project. Valid values:
        # 
        # \\- Draft
        # 
        # \\- Editing
        # 
        # \\- Producing
        # 
        # \\- Produced
        # 
        # \\- ProduceFailed
        # 
        # \\- Deleted
        self.status = status
        # The template ID.
        self.template_id = template_id
        # The template type of the online editing project. Valid values:
        # 
        # \\- Timeline
        # 
        # \\- VETemplate
        self.template_type = template_type
        # The timeline of the online editing project.
        self.timeline = timeline
        # The error message returned if the project conversion failed. The error message displays the detailed information about the failure, and is returned only if the value of TimelineConvertStatus is ConvertFailed.
        self.timeline_convert_error_message = timeline_convert_error_message
        # The project conversion status. Conversion of an API-style timeline into a frontend-style timeline is an asynchronous process and takes effect only if RequestSource:WebSDK is specified.
        # 
        # \\- Unconverted
        # 
        # \\- Converting
        # 
        # \\- Converted
        # 
        # \\- ConvertFailed
        self.timeline_convert_status = timeline_convert_status
        # The title of the online editing project.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_config is not None:
            result['BusinessConfig'] = self.business_config

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.create_source is not None:
            result['CreateSource'] = self.create_source

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.modified_source is not None:
            result['ModifiedSource'] = self.modified_source

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_type is not None:
            result['ProjectType'] = self.project_type

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.timeline_convert_error_message is not None:
            result['TimelineConvertErrorMessage'] = self.timeline_convert_error_message

        if self.timeline_convert_status is not None:
            result['TimelineConvertStatus'] = self.timeline_convert_status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessConfig') is not None:
            self.business_config = m.get('BusinessConfig')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreateSource') is not None:
            self.create_source = m.get('CreateSource')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ModifiedSource') is not None:
            self.modified_source = m.get('ModifiedSource')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('TimelineConvertErrorMessage') is not None:
            self.timeline_convert_error_message = m.get('TimelineConvertErrorMessage')

        if m.get('TimelineConvertStatus') is not None:
            self.timeline_convert_status = m.get('TimelineConvertStatus')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

