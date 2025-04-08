# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class AddImageRequest(TeaModel):
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
        pic_content: str = None,
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
        self.pic_content = pic_content
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
        # > The value cannot contain the following special characters: \\ ¥ $ & %\
        self.str_attr = str_attr
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        # 
        # > The value cannot contain the following special characters: \\ ¥ $ & %\
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.pic_content is not None:
            result['PicContent'] = self.pic_content
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
            self.pic_content = m.get('PicContent')
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


class AddImageAdvanceRequest(TeaModel):
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
        # > The value cannot contain the following special characters: \\ ¥ $ & %\
        self.str_attr = str_attr
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images when you search for images. If you specify this parameter, the response includes this parameter and its value.
        # 
        # > The value cannot contain the following special characters: \\ ¥ $ & %\
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AddImageResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        region: str = None,
    ):
        # The result of category prediction. If a category is specified in the request, the specified category prevails.
        self.category_id = category_id
        # The result of subject identification. The subject area of the image is in the format of `x1,x2,y1,y2`. `x1 and y1` represent the position in the upper-left corner, in pixels. `x2 and y2` represent the position in the lower-right corner, in pixels. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class AddImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        pic_info: AddImageResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The code returned.
        # 
        # *   A value of 0 indicates that the request was successful.
        # *   Values other than 0 indicate that the request failed.
        self.code = code
        # The error message returned if the request failed.
        # 
        # > No value is returned if the request was successful, and an error message is returned if the request failed.
        self.message = message
        # The results of category prediction and subject identification.
        self.pic_info = pic_info
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PicInfo') is not None:
            temp_model = AddImageResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompareSimilarByImageRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        primary_pic_content: str = None,
        secondary_pic_content: str = None,
    ):
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.primary_pic_content = primary_pic_content
        # This parameter is required.
        self.secondary_pic_content = secondary_pic_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CompareSimilarByImageAdvanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        primary_pic_content_object: BinaryIO = None,
        secondary_pic_content_object: BinaryIO = None,
    ):
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.primary_pic_content_object = primary_pic_content_object
        # This parameter is required.
        self.secondary_pic_content_object = secondary_pic_content_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.primary_pic_content_object is not None:
            result['PrimaryPicContent'] = self.primary_pic_content_object
        if self.secondary_pic_content_object is not None:
            result['SecondaryPicContent'] = self.secondary_pic_content_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PrimaryPicContent') is not None:
            self.primary_pic_content_object = m.get('PrimaryPicContent')
        if m.get('SecondaryPicContent') is not None:
            self.secondary_pic_content_object = m.get('SecondaryPicContent')
        return self


class CompareSimilarByImageResponseBodyAccessDeniedDetail(TeaModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action
        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name
        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id
        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type
        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message
        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')
        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')
        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')
        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')
        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')
        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class CompareSimilarByImageResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: CompareSimilarByImageResponseBodyAccessDeniedDetail = None,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        score: float = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.msg = msg
        self.request_id = request_id
        self.score = score
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.score is not None:
            result['Score'] = self.score
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = CompareSimilarByImageResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CompareSimilarByImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompareSimilarByImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CompareSimilarByImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        filter: str = None,
        instance_name: str = None,
        is_delete_by_filter: bool = None,
        pic_name: str = None,
        product_id: str = None,
    ):
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        self.is_delete_by_filter = is_delete_by_filter
        # The name of the image.
        # 
        # *   If this parameter is not set, the system deletes all the images that correspond to the specified ProductId parameter.
        # *   If this parameter is set, the system deletes only the image that is specified by the ProductId and PicName parameters.
        self.pic_name = pic_name
        # The ID of the commodity.
        # 
        # >  A commodity may have multiple images.
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.is_delete_by_filter is not None:
            result['IsDeleteByFilter'] = self.is_delete_by_filter
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IsDeleteByFilter') is not None:
            self.is_delete_by_filter = m.get('IsDeleteByFilter')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class DeleteImageResponseBodyData(TeaModel):
    def __init__(
        self,
        pic_names: List[str] = None,
    ):
        # The name (PicName) of the deleted image.
        self.pic_names = pic_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_names is not None:
            result['PicNames'] = self.pic_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicNames') is not None:
            self.pic_names = m.get('PicNames')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DeleteImageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # The information about the deleted images.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        # The name of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class DetailResponseBodyInstance(TeaModel):
    def __init__(
        self,
        capacity: int = None,
        name: str = None,
        qps: int = None,
        region: str = None,
        service_type: int = None,
        total_count: int = None,
        utc_create: str = None,
        utc_expire_time: str = None,
    ):
        # The capacity of the plan. Unit: × 10,000 images.
        self.capacity = capacity
        # The name of the instance.
        self.name = name
        # The number of queries per second supported by the plan.
        self.qps = qps
        # The information about the region.
        self.region = region
        # The Image Search model.
        # 
        # 0: commodity search. 1: generic image search.
        self.service_type = service_type
        # The number of images.
        self.total_count = total_count
        # The time when the instance was created. Unit: milliseconds.
        self.utc_create = utc_create
        # The time when the instance expires. Unit: milliseconds.
        self.utc_expire_time = utc_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.name is not None:
            result['Name'] = self.name
        if self.qps is not None:
            result['Qps'] = self.qps
        if self.region is not None:
            result['Region'] = self.region
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create
        if self.utc_expire_time is not None:
            result['UtcExpireTime'] = self.utc_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Qps') is not None:
            self.qps = m.get('Qps')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')
        if m.get('UtcExpireTime') is not None:
            self.utc_expire_time = m.get('UtcExpireTime')
        return self


class DetailResponseBody(TeaModel):
    def __init__(
        self,
        instance: DetailResponseBodyInstance = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the instance.
        self.instance = instance
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instance') is not None:
            temp_model = DetailResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DumpMetaRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        # The name of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class DumpMetaResponseBodyData(TeaModel):
    def __init__(
        self,
        dump_meta_status: str = None,
        id: str = None,
    ):
        # The status of the export task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.dump_meta_status = dump_meta_status
        # The ID of the export task.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dump_meta_status is not None:
            result['DumpMetaStatus'] = self.dump_meta_status
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DumpMetaStatus') is not None:
            self.dump_meta_status = m.get('DumpMetaStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DumpMetaResponseBody(TeaModel):
    def __init__(
        self,
        data: DumpMetaResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the export task.
        self.data = data
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DumpMetaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DumpMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DumpMetaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DumpMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DumpMetaListRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the export task.
        self.id = id
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of images to return on each page. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DumpMetaListResponseBodyDataDumpMetaList(TeaModel):
    def __init__(
        self,
        code: str = None,
        id: int = None,
        meta_url: str = None,
        msg: str = None,
        status: str = None,
        utc_create: str = None,
        utc_modified: int = None,
    ):
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # The ID of the task.
        self.id = id
        # The address where you can download the metadata. The address is valid for 2 hours.
        self.meta_url = meta_url
        # The error message returned.
        self.msg = msg
        # The status of the export task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.status = status
        # The time when the task was created. Unit: milliseconds.
        self.utc_create = utc_create
        # The time when the task was updated. Unit: milliseconds.
        self.utc_modified = utc_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.meta_url is not None:
            result['MetaUrl'] = self.meta_url
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create
        if self.utc_modified is not None:
            result['UtcModified'] = self.utc_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MetaUrl') is not None:
            self.meta_url = m.get('MetaUrl')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')
        if m.get('UtcModified') is not None:
            self.utc_modified = m.get('UtcModified')
        return self


class DumpMetaListResponseBodyData(TeaModel):
    def __init__(
        self,
        dump_meta_list: List[DumpMetaListResponseBodyDataDumpMetaList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # A list of tasks that are used to export metadata.
        self.dump_meta_list = dump_meta_list
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The total number of tasks.
        self.total_count = total_count

    def validate(self):
        if self.dump_meta_list:
            for k in self.dump_meta_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DumpMetaList'] = []
        if self.dump_meta_list is not None:
            for k in self.dump_meta_list:
                result['DumpMetaList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dump_meta_list = []
        if m.get('DumpMetaList') is not None:
            for k in m.get('DumpMetaList'):
                temp_model = DumpMetaListResponseBodyDataDumpMetaList()
                self.dump_meta_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DumpMetaListResponseBody(TeaModel):
    def __init__(
        self,
        data: DumpMetaListResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the task that is used to export metadata.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DumpMetaListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DumpMetaListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DumpMetaListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DumpMetaListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IncreaseInstanceRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        callback_address: str = None,
        instance_name: str = None,
        path: str = None,
    ):
        # The name of the Object Storage Service (OSS) bucket.
        # 
        # >  The bucket must be in the same region as the Image Search instance.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The callback address.
        self.callback_address = callback_address
        # The name of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The absolute path to the increment.meta file in the bucket. The path must start with a forward slash (/) and cannot end with a forward slash (/).
        # 
        # This parameter is required.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class IncreaseInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
        increment_status: str = None,
    ):
        # The ID of the task.
        self.id = id
        # The status of the task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.increment_status = increment_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.increment_status is not None:
            result['IncrementStatus'] = self.increment_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IncrementStatus') is not None:
            self.increment_status = m.get('IncrementStatus')
        return self


class IncreaseInstanceResponseBody(TeaModel):
    def __init__(
        self,
        data: IncreaseInstanceResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the task.
        self.data = data
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = IncreaseInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class IncreaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IncreaseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IncreaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IncreaseListRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        id: int = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        path: str = None,
    ):
        # The name of the Object Storage Service (OSS) bucket.
        self.bucket_name = bucket_name
        # The ID of the batch task.
        self.id = id
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of images to return on each page. Default value: 10.
        self.page_size = page_size
        # The absolute path to the increment.meta file in the bucket. The path must start with a forward slash (/) and cannot end with a forward slash (/).
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class IncreaseListResponseBodyDataIncrementsInstance(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        callback_address: str = None,
        code: str = None,
        error_url: str = None,
        id: int = None,
        msg: str = None,
        path: str = None,
        status: str = None,
        utc_create: str = None,
        utc_modified: int = None,
    ):
        # The name of the Object Storage Service (OSS) bucket.
        self.bucket_name = bucket_name
        # The callback address.
        self.callback_address = callback_address
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # The address where you can download the result. The address is valid for 2 hours.
        self.error_url = error_url
        # The ID of the task.
        self.id = id
        # The error message returned.
        self.msg = msg
        # The absolute path to the increment.meta file in the bucket. The path must start with a forward slash (/) and cannot end with a forward slash (/).
        self.path = path
        # The status of the batch task.
        # 
        # *   PROCESSING: in progress
        # *   FAIL: failed
        # *   SUCCESS: successful
        self.status = status
        # The time when the task was created. Unit: milliseconds.
        self.utc_create = utc_create
        # The time when the task was updated. Unit: milliseconds.
        self.utc_modified = utc_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.callback_address is not None:
            result['CallbackAddress'] = self.callback_address
        if self.code is not None:
            result['Code'] = self.code
        if self.error_url is not None:
            result['ErrorUrl'] = self.error_url
        if self.id is not None:
            result['Id'] = self.id
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.path is not None:
            result['Path'] = self.path
        if self.status is not None:
            result['Status'] = self.status
        if self.utc_create is not None:
            result['UtcCreate'] = self.utc_create
        if self.utc_modified is not None:
            result['UtcModified'] = self.utc_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CallbackAddress') is not None:
            self.callback_address = m.get('CallbackAddress')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorUrl') is not None:
            self.error_url = m.get('ErrorUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UtcCreate') is not None:
            self.utc_create = m.get('UtcCreate')
        if m.get('UtcModified') is not None:
            self.utc_modified = m.get('UtcModified')
        return self


class IncreaseListResponseBodyDataIncrements(TeaModel):
    def __init__(
        self,
        instance: List[IncreaseListResponseBodyDataIncrementsInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = IncreaseListResponseBodyDataIncrementsInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class IncreaseListResponseBodyData(TeaModel):
    def __init__(
        self,
        increments: IncreaseListResponseBodyDataIncrements = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # A list of batch tasks.
        self.increments = increments
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The total number of tasks.
        self.total_count = total_count

    def validate(self):
        if self.increments:
            self.increments.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.increments is not None:
            result['Increments'] = self.increments.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Increments') is not None:
            temp_model = IncreaseListResponseBodyDataIncrements()
            self.increments = temp_model.from_map(m['Increments'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class IncreaseListResponseBody(TeaModel):
    def __init__(
        self,
        data: IncreaseListResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the batch task.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = IncreaseListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class IncreaseListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IncreaseListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = IncreaseListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByNameRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        distinct_product_id: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        pic_name: str = None,
        product_id: str = None,
        start: int = None,
    ):
        # The category of the product. For more information, see [Category references](https://help.aliyun.com/document_detail/179184.html).
        # 
        # *   For product search: If a category is specified, the specified category prevails. If no category is specified, the system estimates and selects a category. The category selected by the system is included in the response.
        # *   For generic search: The parameter value is set to 88888888 regardless of whether a category is specified.
        self.category_id = category_id
        self.distinct_product_id = distinct_product_id
        # The filter conditions. int_attr supports the following operators: >, >=, <, <=, and =. str_attr supports the following operators: = and !=. You can set the logical operator between conditions to AND or OR.
        # 
        # Examples:
        # 
        # *   int_attr>=100
        # *   str_attr!="value1"
        # *   int_attr=1000 AND str_attr="value1"
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of images to return on each page. Valid values: 1 to 100. Default value: 10.
        self.num = num
        # The name of the image.
        # 
        # This parameter is required.
        self.pic_name = pic_name
        # The ID of the product.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The number of the image to return. Valid values: 0 to 499. Default value: 0.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.distinct_product_id is not None:
            result['DistinctProductId'] = self.distinct_product_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.num is not None:
            result['Num'] = self.num
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('DistinctProductId') is not None:
            self.distinct_product_id = m.get('DistinctProductId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class SearchImageByNameResponseBodyAuctions(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        custom_content: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_name: str = None,
        product_id: str = None,
        score: float = None,
        sort_expr_values: str = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        # The category of the image.
        self.category_id = category_id
        # The user-defined content.
        self.custom_content = custom_content
        # The attribute, which is an integer.
        self.int_attr = int_attr
        self.int_attr_2 = int_attr_2
        self.int_attr_3 = int_attr_3
        self.int_attr_4 = int_attr_4
        # The name of the image.
        self.pic_name = pic_name
        # The ID of the product.
        self.product_id = product_id
        # The similarity score of the returned image. Valid values: 0 to 1.
        # 
        # >  To use this feature, you must upgrade the SDK to version 3.1.1.
        self.score = score
        # The score information about the image.
        # 
        # > *   This parameter is not supported. We recommend that you use the Score parameter.
        # >*   The SortExprValues parameter indicates a 2-tuple in which values are separated by a semicolon (;). The first value indicates the correlation score of the returned image. A greater value indicates a higher correlation with the sample image. Different algorithms are used.
        # >*   If the value of CategoryId is within the value range from 0 to 2, the value range of SortExprValues is from 0 to 7.33136443711219e+24.
        # >*   If the value of CategoryId is not within the value range from 0 to 2, the value range of SortExprValues is from 0 to 5.37633353624177e+24. If the returned image is identical with the sample image, the highest correlation score is generated.
        self.sort_expr_values = sort_expr_values
        # The attribute, which is a string.
        self.str_attr = str_attr
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2
        if self.int_attr_3 is not None:
            result['IntAttr3'] = self.int_attr_3
        if self.int_attr_4 is not None:
            result['IntAttr4'] = self.int_attr_4
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values
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
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')
        if m.get('IntAttr3') is not None:
            self.int_attr_3 = m.get('IntAttr3')
        if m.get('IntAttr4') is not None:
            self.int_attr_4 = m.get('IntAttr4')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')
        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')
        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')
        return self


class SearchImageByNameResponseBodyHead(TeaModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        # The number of images returned.
        self.docs_found = docs_found
        # The number of images that match the search conditions on the Image Search instance.
        self.docs_return = docs_return
        # The time it takes to complete the search process. Unit: milliseconds.
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageByNameResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the category.
        self.id = id
        # The name of the category.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SearchImageByNameResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        # The result of subject recognition.
        # 
        # The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByNameResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        all_categories: List[SearchImageByNameResponseBodyPicInfoAllCategories] = None,
        category_id: int = None,
        multi_region: List[SearchImageByNameResponseBodyPicInfoMultiRegion] = None,
        region: str = None,
    ):
        # The categories that are supported by the system.
        self.all_categories = all_categories
        # The category selected by the system.
        # 
        # If a category is specified in the request, the specified category prevails.
        self.category_id = category_id
        # The recognized subjects.
        self.multi_region = multi_region
        # The result of subject recognition.
        # 
        # The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region

    def validate(self):
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageByNameResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchImageByNameResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByNameResponseBody(TeaModel):
    def __init__(
        self,
        auctions: List[SearchImageByNameResponseBodyAuctions] = None,
        code: int = None,
        head: SearchImageByNameResponseBodyHead = None,
        msg: str = None,
        pic_info: SearchImageByNameResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The product descriptions returned.
        self.auctions = auctions
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # The summary of the search result.
        self.head = head
        # The error message returned.
        self.msg = msg
        # The information such as the system-selected category and result of subject recognition.
        self.pic_info = pic_info
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageByNameResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Head') is not None:
            temp_model = SearchImageByNameResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageByNameResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchImageByNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchImageByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByPicRequest(TeaModel):
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
        start: int = None,
    ):
        # The category of the product. For more information, see [Category references](https://help.aliyun.com/document_detail/179184.html).
        # 
        # *   For product search: If a category is specified, the specified category prevails. If no category is specified, the system estimates and selects a category. The category selected by the system is included in the response.
        # *   For generic search: The parameter value is set to 88888888 regardless of whether a category is specified.
        self.category_id = category_id
        # Specifies whether to recognize the subject in the image and search for images based on the recognized subject. Valid values: true and false. Default value: true.
        # 
        # *   true: The system recognizes the subject in the image, and searches for images based on the recognized subject. The recognition result is included in the response.
        # *   false: The system does not recognize the subject of the image, and searches for images based on the entire image.
        self.crop = crop
        self.distinct_product_id = distinct_product_id
        # The filter conditions. int_attr supports the following operators: >, >=, <, <=, and =. str_attr supports the following operators: = and !=. You can set the logical operator between conditions to AND or OR.
        # 
        # Examples:
        # 
        # *   int_attr>=100
        # *   str_attr!="value1"
        # *   Example: int_attr=1000 AND str_attr="value1"
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of images to return on each page. Valid values: 1 to 100. Default value: 10.
        self.num = num
        # The image file. The image file is encoded in Base64.
        # 
        # *   The file size of the image cannot exceed 4 MB.
        # *   The following image formats are supported: PNG, JPG, JPEG, BMP, GIF, WebP, TIFF, and PPM.
        # *   The transmission timeout period cannot exceed 5 seconds.
        # *   For brand image searches, the length and the width of the image must range from 200 pixels to 4,096 pixels.
        # *   For cloth image searches, the length and the width of the image must range from 448 pixels to 4,096 pixels.
        # *   For product and generic image searches, the length and the width of the image must range from 100 pixels to 4,096 pixels.
        # *   The image cannot contain rotation settings.
        # 
        # This parameter is required.
        self.pic_content = pic_content
        # The subject area of the image. Specify the subject area in the following format: `x1,x2,y1,y2`. `x1 and y1` represent the upper-left corner pixel. `x2 and y2` represent the lower-right corner pixel.
        # 
        # >*   If you set the Region parameter, the system searches for images based on the value of Region regardless of the value of the Crop parameter.
        self.region = region
        # The number of the image to return. Valid values: 0 to 499. Default value: 0.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class SearchImageByPicAdvanceRequest(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        crop: bool = None,
        distinct_product_id: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        pic_content_object: BinaryIO = None,
        region: str = None,
        start: int = None,
    ):
        # The category of the product. For more information, see [Category references](https://help.aliyun.com/document_detail/179184.html).
        # 
        # *   For product search: If a category is specified, the specified category prevails. If no category is specified, the system estimates and selects a category. The category selected by the system is included in the response.
        # *   For generic search: The parameter value is set to 88888888 regardless of whether a category is specified.
        self.category_id = category_id
        # Specifies whether to recognize the subject in the image and search for images based on the recognized subject. Valid values: true and false. Default value: true.
        # 
        # *   true: The system recognizes the subject in the image, and searches for images based on the recognized subject. The recognition result is included in the response.
        # *   false: The system does not recognize the subject of the image, and searches for images based on the entire image.
        self.crop = crop
        self.distinct_product_id = distinct_product_id
        # The filter conditions. int_attr supports the following operators: >, >=, <, <=, and =. str_attr supports the following operators: = and !=. You can set the logical operator between conditions to AND or OR.
        # 
        # Examples:
        # 
        # *   int_attr>=100
        # *   str_attr!="value1"
        # *   Example: int_attr=1000 AND str_attr="value1"
        self.filter = filter
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of images to return on each page. Valid values: 1 to 100. Default value: 10.
        self.num = num
        # The image file. The image file is encoded in Base64.
        # 
        # *   The file size of the image cannot exceed 4 MB.
        # *   The following image formats are supported: PNG, JPG, JPEG, BMP, GIF, WebP, TIFF, and PPM.
        # *   The transmission timeout period cannot exceed 5 seconds.
        # *   For brand image searches, the length and the width of the image must range from 200 pixels to 4,096 pixels.
        # *   For cloth image searches, the length and the width of the image must range from 448 pixels to 4,096 pixels.
        # *   For product and generic image searches, the length and the width of the image must range from 100 pixels to 4,096 pixels.
        # *   The image cannot contain rotation settings.
        # 
        # This parameter is required.
        self.pic_content_object = pic_content_object
        # The subject area of the image. Specify the subject area in the following format: `x1,x2,y1,y2`. `x1 and y1` represent the upper-left corner pixel. `x2 and y2` represent the lower-right corner pixel.
        # 
        # >*   If you set the Region parameter, the system searches for images based on the value of Region regardless of the value of the Crop parameter.
        self.region = region
        # The number of the image to return. Valid values: 0 to 499. Default value: 0.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.pic_content_object is not None:
            result['PicContent'] = self.pic_content_object
        if self.region is not None:
            result['Region'] = self.region
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
            self.pic_content_object = m.get('PicContent')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class SearchImageByPicResponseBodyAuctions(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        custom_content: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_name: str = None,
        product_id: str = None,
        score: float = None,
        sort_expr_values: str = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        # The category of the image.
        self.category_id = category_id
        # The user-defined content.
        self.custom_content = custom_content
        # The attribute, which is an integer.
        self.int_attr = int_attr
        self.int_attr_2 = int_attr_2
        self.int_attr_3 = int_attr_3
        self.int_attr_4 = int_attr_4
        # The name of the image.
        self.pic_name = pic_name
        # The ID of the product.
        self.product_id = product_id
        # The similarity score of the searched image. Valid values: 0 to 1.
        # 
        # >  To use this feature, you must upgrade the SDK to version 3.1.1.
        self.score = score
        # The score information about the image.
        # 
        # > *   This parameter is not supported. We recommend that you use the Score parameter.
        # >*   The SortExprValues parameter indicates a 2-tuple in which values are separated by a semicolon (;). The first value indicates the correlation score of the returned image. A greater value indicates a higher correlation with the sample image. Different algorithms are used.
        # >*   If the value of CategoryId is within the value range from 0 to 2, the value range of SortExprValues is from 0 to 7.33136443711219e+24.
        # >*   If the value of CategoryId is not within the value range from 0 to 2, the value range of SortExprValues is from 0 to 5.37633353624177e+24. If the returned image is identical with the sample image, the highest correlation score is generated.
        self.sort_expr_values = sort_expr_values
        # The attribute, which is a string.
        self.str_attr = str_attr
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2
        if self.int_attr_3 is not None:
            result['IntAttr3'] = self.int_attr_3
        if self.int_attr_4 is not None:
            result['IntAttr4'] = self.int_attr_4
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
        if self.sort_expr_values is not None:
            result['SortExprValues'] = self.sort_expr_values
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
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')
        if m.get('IntAttr3') is not None:
            self.int_attr_3 = m.get('IntAttr3')
        if m.get('IntAttr4') is not None:
            self.int_attr_4 = m.get('IntAttr4')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('SortExprValues') is not None:
            self.sort_expr_values = m.get('SortExprValues')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')
        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')
        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')
        return self


class SearchImageByPicResponseBodyHead(TeaModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        # The number of images returned.
        self.docs_found = docs_found
        # The number of images that match the search conditions on the Image Search instance.
        self.docs_return = docs_return
        # The time it takes to complete the search process. Unit: milliseconds.
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageByPicResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the category.
        self.id = id
        # The name of the category.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SearchImageByPicResponseBodyPicInfoMultiRegion(TeaModel):
    def __init__(
        self,
        region: str = None,
    ):
        # The result of subject recognition. The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByPicResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        all_categories: List[SearchImageByPicResponseBodyPicInfoAllCategories] = None,
        category_id: int = None,
        multi_region: List[SearchImageByPicResponseBodyPicInfoMultiRegion] = None,
        region: str = None,
    ):
        # The categories that are supported by the system.
        self.all_categories = all_categories
        # The category selected by the system. If a category is specified in the request, the specified category prevails.
        self.category_id = category_id
        # The recognized subjects.
        # 
        # >  To use this feature, you must upgrade the SDK to version 3.1.1.
        self.multi_region = multi_region
        # The result of subject recognition. The subject area of the image, in the format of x1,x2,y1,y2. Specifically, x1 and y1 specify the upper-left pixel, and x2 and y2 specify the lower-right pixel. If a subject area is specified in the request, the specified subject area prevails.
        self.region = region

    def validate(self):
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()
        if self.multi_region:
            for k in self.multi_region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        result['MultiRegion'] = []
        if self.multi_region is not None:
            for k in self.multi_region:
                result['MultiRegion'].append(k.to_map() if k else None)
        if self.region is not None:
            result['Region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageByPicResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        self.multi_region = []
        if m.get('MultiRegion') is not None:
            for k in m.get('MultiRegion'):
                temp_model = SearchImageByPicResponseBodyPicInfoMultiRegion()
                self.multi_region.append(temp_model.from_map(k))
        if m.get('Region') is not None:
            self.region = m.get('Region')
        return self


class SearchImageByPicResponseBody(TeaModel):
    def __init__(
        self,
        auctions: List[SearchImageByPicResponseBodyAuctions] = None,
        code: int = None,
        head: SearchImageByPicResponseBodyHead = None,
        msg: str = None,
        pic_info: SearchImageByPicResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The product descriptions returned.
        self.auctions = auctions
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # The summary of the search result.
        self.head = head
        # The error message returned.
        self.msg = msg
        # The information such as the system-selected category and result of subject recognition.
        self.pic_info = pic_info
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageByPicResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Head') is not None:
            temp_model = SearchImageByPicResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageByPicResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByPicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchImageByPicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchImageByPicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchImageByTextRequest(TeaModel):
    def __init__(
        self,
        distinct_product_id: bool = None,
        filter: str = None,
        instance_name: str = None,
        num: int = None,
        start: int = None,
        text: str = None,
    ):
        self.distinct_product_id = distinct_product_id
        self.filter = filter
        # This parameter is required.
        self.instance_name = instance_name
        self.num = num
        self.start = start
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.distinct_product_id is not None:
            result['DistinctProductId'] = self.distinct_product_id
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.num is not None:
            result['Num'] = self.num
        if self.start is not None:
            result['Start'] = self.start
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistinctProductId') is not None:
            self.distinct_product_id = m.get('DistinctProductId')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Num') is not None:
            self.num = m.get('Num')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class SearchImageByTextResponseBodyAccessDeniedDetail(TeaModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action
        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name
        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id
        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type
        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message
        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')
        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')
        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')
        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')
        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')
        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class SearchImageByTextResponseBodyAuctions(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        custom_content: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_name: str = None,
        product_id: str = None,
        score: float = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        self.category_id = category_id
        self.custom_content = custom_content
        self.int_attr = int_attr
        self.int_attr_2 = int_attr_2
        self.int_attr_3 = int_attr_3
        self.int_attr_4 = int_attr_4
        self.pic_name = pic_name
        self.product_id = product_id
        self.score = score
        self.str_attr = str_attr
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.custom_content is not None:
            result['CustomContent'] = self.custom_content
        if self.int_attr is not None:
            result['IntAttr'] = self.int_attr
        if self.int_attr_2 is not None:
            result['IntAttr2'] = self.int_attr_2
        if self.int_attr_3 is not None:
            result['IntAttr3'] = self.int_attr_3
        if self.int_attr_4 is not None:
            result['IntAttr4'] = self.int_attr_4
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.score is not None:
            result['Score'] = self.score
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
        if m.get('CustomContent') is not None:
            self.custom_content = m.get('CustomContent')
        if m.get('IntAttr') is not None:
            self.int_attr = m.get('IntAttr')
        if m.get('IntAttr2') is not None:
            self.int_attr_2 = m.get('IntAttr2')
        if m.get('IntAttr3') is not None:
            self.int_attr_3 = m.get('IntAttr3')
        if m.get('IntAttr4') is not None:
            self.int_attr_4 = m.get('IntAttr4')
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')
        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')
        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')
        return self


class SearchImageByTextResponseBodyHead(TeaModel):
    def __init__(
        self,
        docs_found: int = None,
        docs_return: int = None,
        search_time: int = None,
    ):
        self.docs_found = docs_found
        self.docs_return = docs_return
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.docs_found is not None:
            result['DocsFound'] = self.docs_found
        if self.docs_return is not None:
            result['DocsReturn'] = self.docs_return
        if self.search_time is not None:
            result['SearchTime'] = self.search_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocsFound') is not None:
            self.docs_found = m.get('DocsFound')
        if m.get('DocsReturn') is not None:
            self.docs_return = m.get('DocsReturn')
        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')
        return self


class SearchImageByTextResponseBodyPicInfoAllCategories(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SearchImageByTextResponseBodyPicInfo(TeaModel):
    def __init__(
        self,
        all_categories: List[SearchImageByTextResponseBodyPicInfoAllCategories] = None,
    ):
        self.all_categories = all_categories

    def validate(self):
        if self.all_categories:
            for k in self.all_categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AllCategories'] = []
        if self.all_categories is not None:
            for k in self.all_categories:
                result['AllCategories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_categories = []
        if m.get('AllCategories') is not None:
            for k in m.get('AllCategories'):
                temp_model = SearchImageByTextResponseBodyPicInfoAllCategories()
                self.all_categories.append(temp_model.from_map(k))
        return self


class SearchImageByTextResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: SearchImageByTextResponseBodyAccessDeniedDetail = None,
        auctions: List[SearchImageByTextResponseBodyAuctions] = None,
        code: int = None,
        head: SearchImageByTextResponseBodyHead = None,
        msg: str = None,
        pic_info: SearchImageByTextResponseBodyPicInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.auctions = auctions
        self.code = code
        self.head = head
        self.msg = msg
        self.pic_info = pic_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.auctions:
            for k in self.auctions:
                if k:
                    k.validate()
        if self.head:
            self.head.validate()
        if self.pic_info:
            self.pic_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()
        result['Auctions'] = []
        if self.auctions is not None:
            for k in self.auctions:
                result['Auctions'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.head is not None:
            result['Head'] = self.head.to_map()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.pic_info is not None:
            result['PicInfo'] = self.pic_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = SearchImageByTextResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m['AccessDeniedDetail'])
        self.auctions = []
        if m.get('Auctions') is not None:
            for k in m.get('Auctions'):
                temp_model = SearchImageByTextResponseBodyAuctions()
                self.auctions.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Head') is not None:
            temp_model = SearchImageByTextResponseBodyHead()
            self.head = temp_model.from_map(m['Head'])
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('PicInfo') is not None:
            temp_model = SearchImageByTextResponseBodyPicInfo()
            self.pic_info = temp_model.from_map(m['PicInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SearchImageByTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchImageByTextResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchImageByTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequest(TeaModel):
    def __init__(
        self,
        custom_content: str = None,
        instance_name: str = None,
        int_attr: int = None,
        int_attr_2: int = None,
        int_attr_3: int = None,
        int_attr_4: int = None,
        pic_name: str = None,
        product_id: str = None,
        str_attr: str = None,
        str_attr_2: str = None,
        str_attr_3: str = None,
        str_attr_4: str = None,
    ):
        # The user-defined content. The value can be up to 4,096 characters in length.
        # 
        # >  If you set this parameter, the response includes this parameter and its value. You can add text such as an image description.
        self.custom_content = custom_content
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The attribute, which is an integer. The attribute can be used to filter images when you search for images. If you set this parameter, the response includes this parameter and its value.
        self.int_attr = int_attr
        self.int_attr_2 = int_attr_2
        self.int_attr_3 = int_attr_3
        self.int_attr_4 = int_attr_4
        # The name of the image. The name can be up to 512 characters in length.
        # 
        # > *   An image is uniquely identified by the values of the ProductId and PicName parameters.
        # >*   If you add an image whose product ID (ProductId) and image name (PicName) are the same as those of an existing image, the newly added image overwrites the existing image.
        # 
        # This parameter is required.
        self.pic_name = pic_name
        # The ID of the product. The ID can be up to 512 characters in length.
        # 
        # >  A product may have multiple images.
        # 
        # This parameter is required.
        self.product_id = product_id
        # The attribute, which is a string. The value can be up to 128 characters in length. The attribute can be used to filter images. If you set this parameter, the response includes this parameter and its value.
        self.str_attr = str_attr
        self.str_attr_2 = str_attr_2
        self.str_attr_3 = str_attr_3
        self.str_attr_4 = str_attr_4

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.pic_name is not None:
            result['PicName'] = self.pic_name
        if self.product_id is not None:
            result['ProductId'] = self.product_id
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
        if m.get('PicName') is not None:
            self.pic_name = m.get('PicName')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('StrAttr') is not None:
            self.str_attr = m.get('StrAttr')
        if m.get('StrAttr2') is not None:
            self.str_attr_2 = m.get('StrAttr2')
        if m.get('StrAttr3') is not None:
            self.str_attr_3 = m.get('StrAttr3')
        if m.get('StrAttr4') is not None:
            self.str_attr_4 = m.get('StrAttr4')
        return self


class UpdateImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        # 
        # *   A value of 0 indicates that the operation is successful.
        # *   Values other than 0 indicate errors.
        self.code = code
        # Id of the request
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


