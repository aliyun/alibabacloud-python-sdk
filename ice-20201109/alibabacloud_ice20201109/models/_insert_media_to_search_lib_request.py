# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertMediaToSearchLibRequest(DaraModel):
    def __init__(
        self,
        images_input: str = None,
        input: str = None,
        media_id: str = None,
        media_type: str = None,
        msg_body: str = None,
        namespace: str = None,
        search_lib_name: str = None,
    ):
        self.images_input = images_input
        # The URL of the video, audio, or image file that you want to import to the search library.
        # 
        # Note: Make sure that you specify a correct file name and the bucket in which the file resides is in the same region where this operation is called. Otherwise, the file cannot be found or the operation may fail.
        # 
        # Specify an Object Storage Service (OSS) URL in the following format: oss://[Bucket name]/[File path]. For example, you can specify oss://[example-bucket-****]/[object_path-****].
        # 
        # Specify an HTTP URL in the following format: public endpoint. For example, you can specify http://example-test-\\*\\*\\*\\*.mp4.
        # 
        # This parameter is required.
        self.input = input
        # The ID of the media asset. Each media ID is unique. If you leave this parameter empty, a media ID is automatically generated for this parameter.
        self.media_id = media_id
        # The type of the media asset. Valid values:
        # 
        # *   video (default)
        # *   image
        # *   audio
        self.media_type = media_type
        # The message body.
        self.msg_body = msg_body
        self.namespace = namespace
        # The name of the search library. Default value: ims-default-search-lib.
        self.search_lib_name = search_lib_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.images_input is not None:
            result['ImagesInput'] = self.images_input

        if self.input is not None:
            result['Input'] = self.input

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.msg_body is not None:
            result['MsgBody'] = self.msg_body

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.search_lib_name is not None:
            result['SearchLibName'] = self.search_lib_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImagesInput') is not None:
            self.images_input = m.get('ImagesInput')

        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('MsgBody') is not None:
            self.msg_body = m.get('MsgBody')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SearchLibName') is not None:
            self.search_lib_name = m.get('SearchLibName')

        return self

