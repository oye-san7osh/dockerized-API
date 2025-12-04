from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StudentPagination(PageNumberPagination):
    
    page_size = 4       # items per page
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 5
    
    
    def get_page_size(self, request):
        
        if request.query_params.get('size'):
            
            return int(request.query_params.get('size'))
        
        return self.page_size
    
    
    def get_paginated_response(self, data):
        
        return Response(
            {
                "status": "success",
                "page_info":
                    {
                        "current_pages": self.page.number,
                        "page_size": self.get_page_size(self.request),
                        "total_items": self.page.paginator.count,
                        "total_pages": self.page.paginator.num_pages,
                    },
                "link":
                    {
                        "next_url": self.get_next_link(),
                        "previous_url": self.get_previous_link(),
                    },
                "results": data
            }
        )
    