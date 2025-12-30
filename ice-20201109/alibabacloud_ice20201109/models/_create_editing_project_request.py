# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEditingProjectRequest(DaraModel):
    def __init__(
        self,
        business_config: str = None,
        clips_param: str = None,
        cover_url: str = None,
        description: str = None,
        material_maps: str = None,
        project_type: str = None,
        template_id: str = None,
        template_type: str = None,
        timeline: str = None,
        title: str = None,
    ):
        # The business configuration of the project. This parameter can be ignored for general editing projects.
        # 
        # For a live stream editing project, observe the following rules: OutputMediaConfig.StorageLocation is required. OutputMediaConfig.Path is optional. If you do not specify this option, the live streaming clips are stored in the root directory by default.
        # 
        # Valid values of OutputMediaTarget include vod-media and oss-object. If you do not specify OutputMediaTarget, the default value oss-object is used.
        # 
        # If you set OutputMediaTarget to vod-media, the setting of OutputMediaConfig.Path does not take effect.
        self.business_config = business_config
        # The material parameter corresponding to the template, in the JSON format. If TemplateId is specified, ClipsParam must also be specified. For more information<props="china">, see [Create and use a regular template](https://help.aliyun.com/document_detail/328557.html) and [Create and use an advanced template](https://help.aliyun.com/document_detail/291418.html).
        self.clips_param = clips_param
        # The thumbnail URL of the online editing project.
        self.cover_url = cover_url
        # The description of the online editing project.
        self.description = description
        # The material associated with the project. Separate multiple material IDs with commas (,). Each type supports up to 10 material IDs.
        self.material_maps = material_maps
        # The type of the editing project. Valid values: EditingProject and LiveEditingProject. A value of EditingProject indicates a regular editing project, and a value of LiveEditingProject indicates a live stream editing project.
        self.project_type = project_type
        # The template ID. This parameter is used to quickly build a timeline with ease. Note: Only one of Timeline and TemplateId can be specified. If TemplateId is specified, ClipsParam must also be specified.
        self.template_id = template_id
        # The template type. This parameter is required if you create a template-based online editing project. Default value: Timeline. Valid values:
        # 
        # *   Timeline: a regular template.
        # *   VETemplate: an advanced template.
        self.template_type = template_type
        self.timeline = timeline
        # The title of the online editing project.
        # 
        # This parameter is required.
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

        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.material_maps is not None:
            result['MaterialMaps'] = self.material_maps

        if self.project_type is not None:
            result['ProjectType'] = self.project_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessConfig') is not None:
            self.business_config = m.get('BusinessConfig')

        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaterialMaps') is not None:
            self.material_maps = m.get('MaterialMaps')

        if m.get('ProjectType') is not None:
            self.project_type = m.get('ProjectType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

