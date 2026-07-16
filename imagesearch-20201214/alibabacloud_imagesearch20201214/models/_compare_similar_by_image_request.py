# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompareSimilarByImageRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        primary_pic_content: str = None,
        secondary_pic_content: str = None,
    ):
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # If you have purchased an Image Search instance, log on to the <props="intl">[Image Search console](https://imagesearch.console.alibabacloud.com)<props="china">[Image Search console](https://imagesearch.console.aliyun.com) to view the instance name.
        # If you have not purchased an Image Search instance, refer to [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # >The instance name is not the instance ID. Make sure you distinguish between them.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The image content.
        # 
        # - The image size must not exceed 4 MB.
        # - Image formats: PNG, JPG, JPEG, BMP, GIF, WEBP, TIFF, and PPM.
        # - The transmission wait time must not exceed 5 seconds.
        # <props="china">
        # - If the service type is product image search, generic image search, furniture image search, or industrial hardware image search, the image width and height must be at least 100 px and at most 4096 px.
        # 
        # <props="china">
        # - If the service type is trademark image search, the image width and height must be at least 200 px and less than 4096 px.
        # 
        # <props="china">
        # - If the service type is fabric image search, the image width and height must be at least 448 px and at most 4096 px.
        # 
        # <props="intl">
        # - If the service type is product image search or generic image search, the image width and height must be at least 100 px and at most 4096 px.
        # 
        # - The image must not contain rotation information.
        # 
        # > **When calling by using an SDK:**- Only V3 SDKs are supported. You do not need to set the PrimaryPicContent field. The SDK encapsulates this field as PrimaryPicContentObject and automatically converts it to Base64 encoding. For examples, refer to [JAVA SDK](https://help.aliyun.com/document_detail/179188.html).- The SDK does not support passing image URLs directly. V3 SDKs provide an alternative way to upload images by URL. For examples, refer to [JAVA SDK](https://help.aliyun.com/document_detail/179188.html).
        # 
        # This parameter is required.
        self.primary_pic_content = primary_pic_content
        # The image content.
        # 
        # - The image size must not exceed 4 MB.
        # - Image formats: PNG, JPG, JPEG, BMP, GIF, WEBP, TIFF, and PPM.
        # - The transmission wait time must not exceed 5 seconds.
        # <props="china">
        # - If the service type is product image search, generic image search, furniture image search, or industrial hardware image search, the image width and height must be at least 100 px and at most 4096 px.
        # 
        # <props="china">
        # - If the service type is trademark image search, the image width and height must be at least 200 px and less than 4096 px.
        # 
        # <props="china">
        # - If the service type is fabric image search, the image width and height must be at least 448 px and at most 4096 px.
        # 
        # <props="intl">
        # - If the service type is product image search or generic image search, the image width and height must be at least 100 px and at most 4096 px.
        # 
        # - The image must not contain rotation information.
        # 
        # > **When calling by using an SDK:**- Only V3 SDKs are supported. You do not need to set the PrimaryPicContent field. The SDK encapsulates this field as PrimaryPicContentObject and automatically converts it to Base64 encoding. For examples, refer to [JAVA SDK](https://help.aliyun.com/document_detail/179188.html).- The SDK does not support passing image URLs directly. V3 SDKs provide an alternative way to upload images by URL. For examples, refer to [JAVA SDK](https://help.aliyun.com/document_detail/179188.html).
        # 
        # This parameter is required.
        self.secondary_pic_content = secondary_pic_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.primary_pic_content is not None:
            result['PrimaryPicContent'] = self.primary_pic_content

        if self.secondary_pic_content is not None:
            result['SecondaryPicContent'] = self.secondary_pic_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PrimaryPicContent') is not None:
            self.primary_pic_content = m.get('PrimaryPicContent')

        if m.get('SecondaryPicContent') is not None:
            self.secondary_pic_content = m.get('SecondaryPicContent')

        return self

