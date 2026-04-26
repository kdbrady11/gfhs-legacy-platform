from django import forms
from django.shortcuts import redirect, render

from .models import ContributionInquiry


class ContributionInquiryForm(forms.ModelForm):
    class Meta:
        model = ContributionInquiry
        fields = [
            "name",
            "email",
            "phone",
            "material_type",
            "material_year",
            "title_or_description",
            "details",
            "permission_acknowledged",
        ]
        widgets = {
            "details": forms.Textarea(attrs={"rows": 5}),
            "permission_acknowledged": forms.CheckboxInput(),
        }
        labels = {
            "name": "Your name",
            "email": "Email address",
            "phone": "Phone number",
            "material_type": "Type of material",
            "material_year": "Approximate year",
            "title_or_description": "Short title or description",
            "details": "Additional details",
            "permission_acknowledged": "I understand this submission is an inquiry and that materials must be reviewed before public display.",
        }


def contribute_materials(request):
    if request.method == "POST":
        form = ContributionInquiryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("contribution_thanks")
    else:
        form = ContributionInquiryForm()

    return render(
        request,
        "inquiries/contribute_materials.html",
        {
            "form": form,
        },
    )


def contribution_thanks(request):
    return render(request, "inquiries/contribution_thanks.html")