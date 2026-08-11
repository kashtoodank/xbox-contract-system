<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Xbox Account Rental Agreement</title>

<style>
body{
    max-width:900px;
    margin:40px auto;
    padding:20px;
    font-family:Arial,sans-serif;
    line-height:1.6;
}

.contract{
    border:1px solid #000;
    padding:30px;
}

input{
    padding:8px;
    margin:5px 0;
    width:100%;
    max-width:500px;
}

canvas{
    border:1px solid #000;
    width:100%;
    max-width:600px;
    height:200px;
}

button{
    padding:12px 24px;
    font-size:16px;
    margin-top:15px;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/signature_pad@4.0.0/dist/signature_pad.umd.min.js"></script>
</head>

<body>

<div class="contract">

<h1 style="text-align:center;">XBOX ACCOUNT RENTAL AGREEMENT</h1>

<form method="POST">

<p>
Date:
<input type="date" name="contract_date" required>
</p>

<p>
This Xbox Account Rental Agreement ("Agreement") is entered into between:
</p>

<p>
<b>Account Owner:</b> elucd
</p>

<p>
<b>Renter:</b><br>
<input type="text" name="full_name" required>
</p>

<h2>1. Rental Account</h2>

<p>
The Account Owner agrees to provide the Renter temporary access to an Xbox account for the rental period stated below.
</p>

<p>
Rental Period: 5 Days<br>
Rental Price: $5.00<br>
Security Deposit: None
</p>

<p>
Rental Start Date: 8/10/26<br>
Rental End Date: 8/15/26
</p>

<h2>2. Permitted Use</h2>

<p>
The Renter may use the Xbox account only for personal use during the rental period.
</p>

<p>
The Renter may make changes to in-game accessories, cosmetic items, animations, or other permitted in-game customizations.
</p>

<h2>3. Account Information</h2>

<p>
The Renter shall not change, remove, add, or modify any account information or security settings.
</p>

<ul>
<li>Password</li>
<li>Email Address</li>
<li>Phone Number</li>
<li>Security Information</li>
<li>Account Recovery Information</li>
<li>Account Ownership Information</li>
<li>Privacy or Security Settings</li>
</ul>

<p>
The account must be returned in substantially the same condition in which it was provided, except for permitted in-game changes.
</p>

<h2>4. Account Access</h2>

<ul>
<li>Share the account with another person</li>
<li>Sell or rent the account to another person</li>
<li>Provide account access to any third party</li>
<li>Attempt to claim ownership of the account</li>
<li>Lock the Account Owner out of the account</li>
</ul>

<h2>5. Breach of Agreement</h2>

<p>
If the Renter violates any term of this Agreement, the Account Owner may immediately terminate the rental.
</p>

<h2>6. Return of Access</h2>

<p>
When the rental period ends, the Renter must immediately stop using the account.
</p>

<h2>7. No Ownership Transfer</h2>

<p>
Ownership remains with the Account Owner at all times.
</p>

<h2>8. Platform Rules</h2>

<p>
Both parties acknowledge that Xbox and Microsoft may maintain their own policies governing account access and use.
</p>

<h2>9. Entire Agreement</h2>

<p>
This Agreement represents the entire understanding between the parties.
</p>

<h2>10. Signatures</h2>

<label>Payhip Order ID</label><br>
<input type="text" name="order_id" required>

<br><br>

<label>Renter Full Legal Name</label><br>
<input type="text" name="legal_name" required>

<br><br>

<label>Renter Email</label><br>
<input type="email" name="email" required>

<br><br>

<label>Phone Number (Optional)</label><br>
<input type="text" name="phone">

<br><br>

<label>Type Your Full Name as Signature</label><br>
<input type="text" name="typed_signature" required>

<br><br>

<label>Draw Signature Below</label><br>

<canvas id="signature-pad" width="600" height="200"></canvas>

<input type="hidden"
       id="signature_data"
       name="signature_data">

<br>

<button type="button" onclick="saveSignature()">
Save Signature
</button>

<br><br>

<label>
<input type="checkbox" required>
I have read and agree to the Xbox Account Rental Agreement.
</label>

<br><br>

<button type="submit">
Submit Agreement
</button>

</form>

</div>

<script>
const canvas = document.getElementById("signature-pad");
const signaturePad = new SignaturePad(canvas);

function saveSignature(){
    document.getElementById("signature_data").value =
        signaturePad.toDataURL();
    alert("Signature saved.");
}
</script>

</body>
</html>
