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
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The material parameters of the template, in the JSON format. If TemplateId is specified, ClipsParam must also be specified. For more information, see [Create and use a regular template](https://help.aliyun.com/document_detail/445399.html) and [Create and use advanced templates](https://help.aliyun.com/document_detail/445389.html).
        self.clips_param = clips_param
        # The parameters for editing and production. For more information, see [EditingProduceConfig](https://help.aliyun.com/document_detail/357745.html).
        # 
        # >  If no thumbnail is specified in EditingProduceConfig, the first frame of the video is used as the thumbnail.
        # 
        # *   AutoRegisterInputVodMedia: specifies whether to automatically register the ApsaraVideo VOD media assets in your timeline with IMS. Default value: true.
        # *   OutputWebmTransparentChannel: specifies whether the output video contains alpha channels. Default value: false.
        # *   CoverConfig: the custom thumbnail parameters.
        # *
        self.editing_produce_config = editing_produce_config
        # The metadata of the produced video, in the JSON format. For more information about the parameters, see [MediaMetadata](https://help.aliyun.com/document_detail/357745.html).
        self.media_metadata = media_metadata
        # The configurations of the output file, in the JSON format. You can specify an OSS URL or a storage location in a storage bucket of ApsaraVideo VOD.
        # 
        # To store the output file in OSS, you must specify MediaURL. To store the output file in ApsaraVideo VOD, you must specify StorageLocation and FileName.
        # 
        # For more information, see [OutputMediaConfig](https://help.aliyun.com/document_detail/357745.html).
        # 
        # This parameter is required.
        self.output_media_config = output_media_config
        # The type of the output file. Valid values:
        # 
        # *   oss-object: OSS object in an OSS bucket.
        # *   vod-media: media asset in ApsaraVideo VOD.
        # *   S3: output file based on the Amazon Simple Storage Service (S3) protocol.
        self.output_media_target = output_media_target
        # The ID of the editing project.
        # 
        # > : You must specify one of ProgectId, Timeline, and TempalteId and leave the other two parameters empty.
        self.project_id = project_id
        # The metadata of the editing project, in the JSON format. For more information about the parameters, see [ProjectMetadata](https://help.aliyun.com/document_detail/357745.html).
        self.project_metadata = project_metadata
        # The source of the editing and production request. Valid values:
        # 
        # *   OpenAPI
        # *   AliyunConsole
        # *   WebSDK
        self.source = source
        # The template ID. The template is used to build a timeline with ease.
        # 
        # > : You must specify one of ProgectId, Timeline, and TempalteId and leave the other two parameters empty. If TemplateId is specified, ClipsParam must also be specified.
        self.template_id = template_id
        self.timeline = timeline
        # The user-defined data in the JSON format, which can be up to 512 bytes in length. You can specify a custom callback URL. For more information, see [Configure a callback upon editing completion](https://help.aliyun.com/document_detail/451631.html).
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

