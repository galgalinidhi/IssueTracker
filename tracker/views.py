from django.shortcuts import render

# Create your views here.
# @api_view(['POST'])
# def create_issue(request):
#     if request.method == 'POST':
#         serializer = IssueSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_issue_details(request, issue_id):
#     try:
#         issue = Issue.objects.get(id=issue_id)
#     except Issue.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = IssueSerializer(issue)
#         return Response(serializer.data)

# @api_view(['PUT'])
# def update_issue(request, issue_id):
#     try:
#         issue = Issue.objects.get(id=issue_id)
#     except Issue.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = IssueSerializer(issue, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Delete an issue by its ID
# @api_view(['DELETE'])
# def delete_issue(request, issue_id):
#     try:
#         issue = Issue.objects.get(id=issue_id)
#     except Issue.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'DELETE':
#         issue.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
