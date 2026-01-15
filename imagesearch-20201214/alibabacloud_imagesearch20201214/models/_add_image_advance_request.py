# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class AddImageAdvanceRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        custom_content: str = None,
        instance_name: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_content_object: BinaryIO = None,
        pic_name: str = None,
        product_id: str = None,
        region: str = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        # The category of the image. For more information, see [Category reference](https://help.aliyun.com/document_detail/179184.html).
        # 
        # > *   For product image search, if you specify a category for an image, the specified category prevails. If you do not specify a category for an image, the system predicts the category, and returns the prediction result in the response.
        # >*   For generic image search, only 88888888 may be returned for this parameter in the response regardless of whether a category is specified.
        self.category_id = category_id
        # Specifies whether to identify the subject in the image and search for images based on the subject identification result. Default value: true. Valid values:
        # 
        # *   true: The system identifies the subject in the image, and searches for images based on the subject identification result. The subject identification result is included in the response.
        # *   false: The system does not identify the subject in the image, and searches for images based on the entire image.
        self.crop = crop
        # The user-defined content. The value can be up to 4,096 characters in length.
        # 
        # > If you specify this parameter, the response includes this parameter and its value. You can add text such as an image description.
        self.custom_content = custom_content
        # The name of the Image Search instance. The name can be up to 20 characters in length. If an Image Search instance is purchased, you can log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance. If no Image Search instance is purchased, you must purchase an instance. For more information, see [Activate Image Search](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # 
        # > The instance name is not the instance ID.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The attribute, which is an integer. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        self.int_attr = int_attr
        # The attribute, which is an integer. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        self.int_attr_2 = int_attr_2
        self.int_attr_3 = int_attr_3
        self.int_attr_4 = int_attr_4
        # The image file. The image file is encoded in Base64.
        # 
        # *   The file size of the image cannot exceed 4 MB.
        # *   The following image formats are supported: PNG, JPG, JPEG, BMP, GIF, WebP, TIFF, and PPM.
        # *   The transmission timeout period cannot exceed 5 seconds.
        # *   For product and generic image searches, the length and width of the image must range from 100 pixels to 4,096 pixels.
        # *   The image cannot contain rotation settings.
        # 
        # > *   If you use SDKs to call this operation, you do not need to specify **PicContent**. The SDKs encapsulate this parameter and automatically encode its value in Base64. For more information about how to use Image Search SDK for Java, see [Java SDK](https://help.aliyun.com/document_detail/179188.html).
        # >*   If you use OpenAPI Explorer to call this operation, you can select only the **2019-03-25** version. If you call this operation of other versions, the value of **PicContent** cannot be encoded in Base64.
        # 
        # This parameter is required.
        self.pic_content_object = pic_content_object
        # The name of the image. The name can be up to 512 characters in length.
        # 
        # > *   An image is uniquely identified by the values of ProductId and PicName.
        # >*   If you add an image whose product ID (ProductId) and image name (PicName) are the same as those of an existing image, the newly added image overwrites the existing image.
        # 
        # This parameter is required.
        self.pic_name = pic_name
        # The ID of the product. The ID can be up to 512 characters in length.
        # 
        # > A product may have multiple images.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The subject area of the image, in the format of `x1,x2,y1,y2`. `x1 and y1` represent the position in the upper-left corner, in pixels. `x2 and y2` represent the position in the lower-right corner, in pixels.
        # 
        # > *   If you specify Region, the system searches for images based on the value of Region regardless of the value of Crop.
        # >*   The value of Region does not have a unit. The value is generated based on the length and width of the image. If the length and width of the image are scaled, the value of Region must be proportionally adjusted.
        self.region = region
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        # 
        # > The value cannot contain the following special characters: \\ ¥ $ & %
        self.str_attr = str_attr
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        # 
        # > The value cannot contain the following special characters: \\ ¥ $ & %
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.crop is not None:
            result['Crop'] = self.crop

        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr

        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2

        if self.int_attr_3 is not None:
            result['IntAttr3'] = self.int_attr_3

        if self.int_attr_4 is not None:
            result['IntAttr4'] = self.int_attr_4

        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object

        if self.pic_name is not None:
            result['PicName'] = self.pic_name

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region is not None:
            result['Region'] = self.region

        if self.str_attr is not None:
            result['StrAttr'] = self.str_attr

        if self.str_attr_2 is not None:
            result['StrAttr2'] = self.str_attr_2

        if self.str_attr_3 is not None:
            result['StrAttr3'] = self.str_attr_3

        if self.str_attr_4 is not None:
            result['StrAttr4'] = self.str_attr_4

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')

        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')

        if m.get('IntAttr3') is not None:
            self.int_attr_3 = m.get('IntAttr3')

        if m.get('IntAttr4') is not None:
            self.int_attr_4 = m.get('IntAttr4')

        if m.get('PicContent') is not None:
            self.pic_content_object = m.get('PicContent')

        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')

        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')

        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')

        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')

        return self

