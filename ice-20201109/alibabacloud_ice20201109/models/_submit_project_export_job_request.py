# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitProjectExportJobRequest(DaraModel):
    def __init__(
        self,
        export_type: str = None,
        output_media_config: str = None,
        project_id: str = None,
        timeline: str = None,
        user_data: str = None,
    ):
        # The export type. Valid values:
        # 
        # *   **BaseTimeline**: exports the timeline.
        # *   **AdobePremierePro**: exports an Adobe Premiere Pro project.
        self.export_type = export_type
        # The output path for the exported project and generated intermediate files, in JSON format. The export destination only supports OSS. Path fields:
        # 
        # *   **Bucket**: Required. The OSS bucket name.
        # *   **Prefix**: Optional. The path prefix. If not specified, it defaults to the root directory.
        # *   **Width**: Optional. The width of the output. The value must be a positive integer. If not provided, the system automatically calculates the value based on the input project or timeline.
        # *   **Height**: Optional. The height of the output. The value must be a positive integer. If not provided, the system automatically calculates the value based on the input project or timeline.
        # 
        # This parameter is required.
        self.output_media_config = output_media_config
        # The ID of the online editing project.
        # >Notice: Either ProjectId or Timeline must be provided.
        self.project_id = project_id
        # The timeline of the online editing job. For data structure, see [Timeline](https://help.aliyun.com/document_detail/198823.html).
        # >Notice: Either ProjectId or Timeline must be provided.
        self.timeline = timeline
        # The user-defined data in the JSON format.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.output_media_config is not None:
            result['OutputMediaConfig'] = self.output_media_config

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('OutputMediaConfig') is not None:
            self.output_media_config = m.get('OutputMediaConfig')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

