from scrapy import Request;
from scrapy.exceptions import DropItem;
from scrapy.pipelines.images import ImagesPipeline;

class ImagePipeline(ImagesPipeline):
    def file_path(self, requset, response=None, info=None):
        url = requset.url;
        file_name = url.split("/")[-1];
        return file_name;

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok];
        if not image_path:
            raise DropItem("image download Failed");
        return item;

    def get_media_requests(self, item, info):
        yield Request(item["url"]);
