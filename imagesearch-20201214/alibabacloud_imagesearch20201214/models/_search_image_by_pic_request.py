# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchImageByPicRequest(DaraModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        distinct_product_id: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        pic_content: str = None,
        region: str = None,
        score_threshold: str = None,
        start: int = None,
    ):
        # The product category. For more information, see [Category reference](https://help.aliyun.com/document_detail/179184.html).
        #  - For product image search, if you specify a category, the specified category is used. If you do not specify a category, the system predicts the category. You can obtain the predicted category from the response.
        # <props="china">
        #  - For fabric, trademark, generic furniture, and industrial hardware image search, the system sets the category to 88888888 regardless of whether you specify a category.
        # 
        # <props="intl">
        #  - For generic image search, the system sets the category to 88888888 regardless of whether you specify a category.
        # .
        self.category_id = category_id
        # Specifies whether to perform subject identification. Default value: true.
        #  - If this parameter is set to true, the system performs subject identification and searches based on the identified subject. You can obtain the subject identification result from the response.
        #  - If this parameter is set to false, the system does not perform subject identification and searches based on the entire image.
        # <props="china">
        # - For fabric image search, this parameter is ignored and the system searches based on the entire image.
        # .
        self.crop = crop
        # Specifies whether to deduplicate results based on the ProductId field during the search. If this parameter is set to true, deduplication is performed.
        self.distinct_product_id = distinct_product_id
        # The filter condition. The int_attr field supports the following operators: in, not in, greater than (>), greater than or equal to (>=), less than (<), less than or equal to (<=), and equal to (=). The str_attr field supports the following operators: in, not in, equal to (=), and not equal to (!=). Multiple conditions can be connected by using AND and OR.
        # Examples:
        # - int_attr >= 100.
        # - str_attr != "value1".
        # - int_attr = 1000 AND str_attr = "value1".
        # 
        # >A maximum of 4096 characters are supported.
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # If you have purchased an Image Search instance, log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance name.
        # If you have not purchased an Image Search instance, see [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # >The instance name is not the instance ID. Make sure that you distinguish between them.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of results to return. Valid values: 1 to 100. Default value: 10.
        self.num = num
        # The image content.
        #  - The image size cannot exceed 4 MB.
        #  - Image formats: PNG, JPG, JPEG, BMP, GIF, WEBP, TIFF, and PPM.
        #  - The transmission wait time cannot exceed 5 seconds.
        # <props="china">
        #  - For product image search, generic image search, furniture image search, and industrial hardware image search, the image width and height must be greater than or equal to 100 px and less than or equal to 4096 px.
        # For trademark image search, the image width and height must be greater than or equal to 200 px and less than 4096 px.
        # For fabric image search, the image width and height must be greater than or equal to 448 px and less than or equal to 4096 px.
        # 
        # <props="intl">
        #  - For product image search and generic image search, the image width and height must be greater than or equal to 100 px and less than or equal to 4096 px.
        # 
        # - The image cannot contain rotation information.
        # 
        # > - **Call by using the SDK:**
        #   - If you use the V3 SDK, you do not need to specify the PicContent field. The SDK encapsulates this field as PicContentObject and automatically converts it to Base64 encoding. For specific examples, see [Java SDK](https://help.aliyun.com/document_detail/179188.html).
        #   - The SDK does not support directly passing an image URL. The V3 SDK provides an alternative method to upload images by URL. For specific examples, see [Java SDK](https://help.aliyun.com/document_detail/179188.html).
        # - **Call by using the Alibaba Cloud OpenAPI platform:**
        #   - If you use the **2019-03-25** version, set the **PicContent** field to the **Base64**-encoded string of the image.
        #   - If you use the **2020-12-14** version, click the upload button in the **PicContent** field to upload the image.
        # 
        # This parameter is required.
        self.pic_content = pic_content
        # The subject region of the image, in the format of `x1,x2,y1,y2`, where `x1,y1` is the upper-left point and `x2,y2` is the lower-right point.
        # > - If you specify Region, the system searches based on the specified Region regardless of the value of the Crop parameter.
        # <props="china">
        # - For fabric image search, this parameter is ignored and the system searches based on the entire image.
        # .
        self.region = region
        # The similarity score threshold. After you specify this threshold, only images with a similarity score greater than or equal to the threshold are returned. Valid values: 0.00 to 1.00. Up to two decimal places are supported. Default value: 0.00.
        self.score_threshold = score_threshold
        # The start position of the results to return. Valid values: 0 to 499. Default value: 0.
        self.start = start

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

        if self.distinct_product_id is not None:
            result['DistinctProductId'] = self.distinct_product_id

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.num is not None:
            result['Num'] = self.num

        if self.pic_content is not None:
            result['PicContent'] = self.pic_content

        if self.region is not None:
            result['Region'] = self.region

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('Crop') is not None:
            self.crop = m.get('Crop')

        if m.get('DistinctProductId') is not None:
            self.distinct_product_id = m.get('DistinctProductId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        if m.get('PicContent') is not None:
            self.pic_content = m.get('PicContent')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

