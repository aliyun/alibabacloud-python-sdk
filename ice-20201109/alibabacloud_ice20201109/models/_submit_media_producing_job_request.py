# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitMediaProducingJobRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        clips_param: str = None,
        editing_produce_config: str = None,
        media_metadata: str = None,
        output_media_config: str = None,
        output_media_target: str = None,
        project_id: str = None,
        project_metadata: str = None,
        source: str = None,
        template_id: str = None,
        timeline: str = None,
        user_data: str = None,
    ):
        # A client-generated token that ensures request idempotence. This token must be a unique value of up to 64 ASCII characters.
        self.client_token = client_token
        # The clip parameters that correspond to the template, in JSON format. If `TemplateId` is specified, this parameter is required. For details about the format, see [Create and use basic templates](https://help.aliyun.com/document_detail/445399.html) and [Create and use advanced templates](https://help.aliyun.com/document_detail/445389.html).
        self.clips_param = clips_param
        # The parameters for the media producing job. For configuration details, see [EditingProduceConfig parameter details](~~357745#section-8a4-pb2-hkv~~).
        # 
        # > If a cover is not configured in `EditingProduceConfig`, the first frame of the video is used as the default cover.
        # 
        # - `AutoRegisterInputVodMedia`: Specifies whether to automatically register the VOD media assets in your timeline to IMS. Default value: true.
        # 
        # - `OutputWebmTransparentChannel`: Specifies whether to output a video with a transparent channel. Default value: false.
        # 
        # - `CoverConfig`: The parameters for a custom cover.
        # 
        # - ...
        self.editing_produce_config = editing_produce_config
        # The metadata of the output video, in JSON format. For details about the structure, see [MediaMetadata](~~357745#97ff26d0e3c28~~).
        self.media_metadata = media_metadata
        # The configuration for the output media target, in JSON format. You can set the URL for the output media in OSS or the storage location in a VOD bucket.
        # 
        # - When outputting to OSS, the `MediaURL` parameter is required.
        # 
        # - When outputting to VOD, both the `StorageLocation` and `FileName` parameters are required.
        # 
        # For more information, see [OutputMediaConfig parameter examples](~~357745#title-4j6-ve7-g31~~).
        # 
        # This parameter is required.
        self.output_media_config = output_media_config
        # The target type for the output media. Valid values:
        # 
        # - `oss-object`: An object in your Alibaba Cloud OSS bucket.
        # 
        # - `vod-media`: A media asset in Alibaba Cloud VOD.
        # 
        # - `S3`: A destination that supports the S3 protocol.
        self.output_media_target = output_media_target
        # The ID of the editing project. Call the [CreateEditingProject](https://help.aliyun.com/document_detail/441137.html) operation to create an editing project and obtain the `ProjectId` to submit a media producing job.
        # >Notice: You must specify one of the `ProjectId`, `Timeline`, or `TemplateId` parameters. The other two parameters must be left empty.
        self.project_id = project_id
        # The metadata of the editing project, in JSON format. For details about the structure, see [ProjectMetadata](~~357745#title-yvp-81k-wff~~).
        self.project_metadata = project_metadata
        # The source of the media producing job request. Valid values:
        # 
        # - `OpenAPI`: A request initiated through an API call.
        # 
        # - `AliyunConsole`: A request that originates from the Alibaba Cloud console.
        # 
        # - `WebSDK`: A request sent from a front-end page that integrates the WebSDK.
        self.source = source
        # The ID of a template for quickly building a timeline. You can use basic and advanced templates for video editing.
        # 
        # - When you submit a media producing job using a template ID, you must provide the `ClipsParam` parameter to adjust or replace clips in the template.
        # 
        # - Call the [GetTemplate](https://help.aliyun.com/document_detail/441164.html) operation to obtain template information.
        # 
        # >Notice: 
        # 
        # You must specify one of the `ProjectId`, `Timeline`, or `TemplateId` parameters. The other two parameters must be left empty.
        self.template_id = template_id
        # The timeline for the cloud editing job. To arrange clips and design effects, manually construct the `Timeline` parameter.
        # 
        # - A timeline primarily consists of three types of objects: tracks, clips, and effects. For more information, see [Timeline configuration](https://help.aliyun.com/document_detail/198823.html).
        # 
        # - For more examples of timeline configurations, see [Best practices](https://help.aliyun.com/document_detail/2766669.html).
        # 
        # >Notice: 
        # 
        # You must specify one of the `ProjectId`, `Timeline`, or `TemplateId` parameters. The other two parameters must be left empty.
        self.timeline = timeline
        # Custom user data in JSON format. The value can be up to 512 bytes in length. This parameter supports [job completion callback configuration](https://help.aliyun.com/document_detail/451631.html). The fields include:
        # 
        # - `NotifyAddress`: The callback for job completion.
        # 
        # - `RegisterMediaNotifyAddress`: The callback invoked when the analysis of the output media asset is complete.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.clips_param is not None:
            result['ClipsParam'] = self.clips_param

        if self.editing_produce_config is not None:
            result['EditingProduceConfig'] = self.editing_produce_config

        if self.media_metadata is not None:
            result['MediaMetadata'] = self.media_metadata

        if self.output_media_config is not None:
            result['OutputMediaConfig'] = self.output_media_config

        if self.output_media_target is not None:
            result['OutputMediaTarget'] = self.output_media_target

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_metadata is not None:
            result['ProjectMetadata'] = self.project_metadata

        if self.source is not None:
            result['Source'] = self.source

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ClipsParam') is not None:
            self.clips_param = m.get('ClipsParam')

        if m.get('EditingProduceConfig') is not None:
            self.editing_produce_config = m.get('EditingProduceConfig')

        if m.get('MediaMetadata') is not None:
            self.media_metadata = m.get('MediaMetadata')

        if m.get('OutputMediaConfig') is not None:
            self.output_media_config = m.get('OutputMediaConfig')

        if m.get('OutputMediaTarget') is not None:
            self.output_media_target = m.get('OutputMediaTarget')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectMetadata') is not None:
            self.project_metadata = m.get('ProjectMetadata')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

